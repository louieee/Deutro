<h2>Project Description</h2>

This Project is a complete django management system starter template to enable young django developers easily start up their own several management systems.
It consists of 

<ul>
<li>
    Redis 
</li>
<li>
    Celery
</li>
<li>
    Django Multitenant
</li>
<li>
    Django Channels
</li>
<li>
    Django Hosts ( for multiple domains)
</li>
<li>
    Django Rest API
</li>
</ul>

PS: More updates will be coming from time to time.


<h2>
    Project Setup
</h2>

<ul>
    <li>Clone the repository.</li>
    <li>Set up your virtual environment.</li>
    <li>Run <code>pip install -r requirements.txt</code></li>
    <li>Run  <code>python manage.py migrate</code></li>
    <li>Run <code>python manage.py create_domains</code></li>
    <ul>
        <li>Domains should be <code>localhost</code>
        <li>Name should be <code>LocalHost</code> or virtually whatever you want.</li>
    </ul>
    <li>run <code>python manage.py createsuperuser</code></li>
    <li>run <code>python manage.py runserver</code> </li>
    <li> visit <code>admin.localhost:8000</code> to login to the admin dashboard</li>
</ul>



