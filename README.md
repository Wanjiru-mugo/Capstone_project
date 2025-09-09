# Capstone_project
The Pet Insurance API - http://127.0.0.1:8000/

**Project Objective:**
This is a backend API that helps Kenyan pet owners conviniently find the right pet insurance by providing details on cover plans, benefits, deductibles, premium costs, and vetrinary provider networks in the Kenyan market. 

**Technologies used**
-Python
-Django
-Django Rest Framework
-MySQL

**DEVELOPMENT WORKFLOW**
1. Initialised Django project - pet_insurance_api
2. Created a feature branch for the next development phase - database-models
3. Initialised/created Django app - pet_cover

**DATABASE MODELS & SAMPLE DATA**
Created 5 models:
    1. InsuranceCompany - stores info on insurance providers
        Takes attributes - name, contact_email, description
    2. Plan - stores info about a specific insurance plan
        Takes attributes - name, insurance_company, premium, deductible, copay, waiting_period, annual_limit, vet_clinic
    3. Benefit - stores the benefits of a plan
        Takes attributes - name, description, plans
    4. ExclusiveOf - stores what a plan does not cover 
        Takes attributes - name, description, plans
    5. VetClinic - displays veterinary clinics in the network
        Takes attributes - name, address, contact_phone

Model Relationships Definition:
    **One-to-many**: a single insurance company can have many plans (creates a ForeignKey field on the Plan model)
    **Many-to-many**: a plan can have many benefits and a benefit can belong to many plans; 
        a plan can have many exclusions while a single exclusion can belong to many plans; 
        a plan can be associated with many vet clinics and a vet clinin can offer many plans
    
Benefits, exclusions, vet clinics data were created from the Django shell.

**SET UP ADMIN INTERFACE**
Admin interface login details:
    email - wanjirumugo@gmail.com
    username - Wanjiru
    password - 123456
Data seeding from admin interface
Customise admin interface models:
    Plan - filter by insurance company
    Benefit - filter and search by name
    VetClinic - filter and search by address and name
    ExclusiveOf - filter by name

**SETUP SERIALIZERS FOR MODELS**
**InsuranceCompanySerializer**: a representation of each insurance company including their related plans.
**PlanSerializer**: a representation of each plan, including nested representation of related benefits, exclusions, and vetclinic service. 
    **Custome Validation Value**:
        For data integrity, a 400Error will be raised should the premium value be greater than the annual limit. 
**BenefitSerializer**: a representation of each benefit and its description
**ExclusiveOfSerializer**: a representation of each exclusion and its description
**VetClinicSerializer**: a representation of each vet clinic, its location, and contact phone

**STATIC FILES**
The API has the following static files in the static directory:
    scripts.js
    styles.css
    base.html

**USER ROLES AND PERMISSIONS**
The API implements permission class IsAdminOrReadOnly which allows admin and users functionality as follows:
        1. Admin users have full CRUD operations access on all models
        2. Regular users have only read-only access and can retrive data using GET, HEAD, OPTIONS request. They cannot manipulate the models. 

**API VIEWS**
The API uses the following ViewSets:
        1. InsuranceCompanyViewSet - handles all CRUD operations for the insurance companies for admin and read-only for users
        2. PlanViewSet - all CRUD operations for plans model for the admin but read-only for regular users.
        Includes a search filter for 'insurance_company', and 'vet_clinic'
        Includes a data filter by 'insurance_company'
        3. BenefitViewSet - handles all CRUD operations for benefit instances for the admin but read-only for regular users
        4. ExclusiveOfViewSet - handles all CRUD operations for exclusion instances for admin but read-only for regular users
        5. VetClinicViewSet - handles all CRUD operations for vet clinic instances for admin but read-only for regular users. Includes a search filter for 'name' and 'address' fields.

**URL MAPPING**
Using the automatic URL router, the following endpoints were generated:
    1.*/api/* the API root for all existing endpoints
    2. *GET /api/insurance_companies/* lists all pet insurance companies
    3. *GET /api/insurance_companies/{id}/* retrieve the details of a single insurance company
    4. *GET /api/plans/* lists all available plans
    5. *GET /api/benefits/* lists all available benefits 
    6. *GET /api/exclusive_of/* lists all exclusions
    7. *GET /api/vet_clinics/* lists all vet clinics. Allows search by name or address
    8. *POST /api/token/* obtains token from admin user
    9. *POST /api-auth/login/ authenticates a login session. 
    10. *POST /api-auth/logout/* authenticates a logout session

    
