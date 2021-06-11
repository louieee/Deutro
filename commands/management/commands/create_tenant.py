import sys
from django.core import exceptions
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import capfirst
from school.models import School


class NotRunningInTTYException(Exception):
    pass


class Command(BaseCommand):
    help = 'Used to create a tenant.'
    requires_migrations_checks = True
    stealth_options = ('stdin',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TenantModel = School
        self.nameField = School._meta.get_field('name')
        self.domainField = School._meta.get_field('domain_url')
        self.schemaField = School._meta.get_field('schema_name')

    def add_arguments(self, parser):
        parser.add_argument(
            '--%s' % 'name',
            dest='name', default=None,
            help='Specifies the domain.',
        )
        parser.add_argument(
            '--%s' % 'schema',
            dest='schema', default=None,
            help='Specifies the schema name.',
        )
        parser.add_argument(
            '--%s' % 'domain', dest='domain', default=None,
            help='Specifies the domain url.',
        )

    def execute(self, *args, **options):
        self.stdin = options.get('stdin', sys.stdin)  # Used for testing
        return super().execute(*args, **options)

    def handle(self, *args, **options):
        name = options['name']
        schema = options['schema']
        domain = options['domain']
        verbose_domain_field = self.domainField.verbose_name
        verbose_name_field = self.nameField.verbose_name
        verbose_schema_field = self.schemaField.verbose_name
        # Enclose this whole thing in a try/except to catch
        # KeyboardInterrupt and exit gracefully.
        try:
            if hasattr(self.stdin, 'isatty') and not self.stdin.isatty():
                raise NotRunningInTTYException("Not running in a TTY")
            name = self.collect_data(verbose_field=verbose_name_field, field=self.nameField, field_name='name')
            domain = self.collect_data(verbose_field=verbose_domain_field, field=self.domainField, field_name='domain_url')
            schema = self.collect_data(verbose_field=verbose_schema_field, field=self.schemaField, field_name='schema_name')

        except KeyboardInterrupt:
            self.stderr.write("\nOperation cancelled.")
            sys.exit(1)
        except NotRunningInTTYException:
            self.stdout.write(
                "Tenant creation skipped due to not running in a TTY. "
            )
        if domain and name and schema:
            tenant_data = {
                'domain_url': domain,
                'name': name,
                'schema_name': schema
            }
            self.TenantModel(**tenant_data).save()
            if options['verbosity'] >= 1:
                self.stdout.write("Tenant created successfully.")

    def get_input_data(self, field, message, default=None):
        """
        Override this method if you want to customize data inputs or
        validation exceptions.
        """
        raw_value = input(message)
        if default and raw_value == '':
            raw_value = default
        try:
            val = field.clean(raw_value, None)
        except exceptions.ValidationError as e:
            self.stderr.write("Error: %s" % '; '.join(e.messages))
            val = None
        return val

    def collect_data(self, verbose_field, field, field_name, item=None):
        while item is None:
            input_msg = '%s: ' % capfirst(verbose_field)
            item = self.get_input_data(field, input_msg)
            if not item:
                continue
            if field.unique:
                try:
                    data = {field_name: item}
                    self.TenantModel.objects.get(**data)
                except self.TenantModel.DoesNotExist:
                    pass
                else:
                    self.stderr.write("Error: That %s is already in use." % verbose_field)
                    item = None
        if not item:
            raise CommandError('%s cannot be blank.' % capfirst(verbose_field))
        return item



