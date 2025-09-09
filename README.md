# Capstone_project
The Pet Insurance API

**Project Objective:**
This is a backend API that helps Kenyan pet owners conviniently find the right pet insurance by providing details on cover plans, benefits, deductibles, premium costs, and vetrinary provider networks in the Kenyan market. 

**Technologies used**
-Python
-Django
-Django Rest Framework
-MySQL

**DEVELOPMENT WORKFLOW**
1. Intialised Django project - pet_insurance_api
2. Created a feature branch for the next development phase - database-models
3. Intialised/created Django app - pet_cover

**DATABASE MODELS & SAMPLE DATA**
Created 5 models:
    1. InsuranceCompany - stores info on insurance providers
    2. Plan - stores info about a specific insurance plan
    3. Benefit - stores the benefits of a plan
    4. ExclusiveOf - stores what a plan does not cover 
    5. VetClinic - displays veterinary clinics in the network

Model Relationships Definition:
    **One-to-many**: a single insurance company can have many plans (creates a ForeignKey field on the Plan model)
    **Many-to-many**: a plan can have many benefits and a benefit can belong to many plans; 
        a plan can have many exclusions while a single exclusion can belong to many plans; 
        a plan can be associated with many vet clinics and a vet clinin can offer many plans
    
Benefits, exclusions, vet clinics data were created from the Django shell.

**SET UP ADMIN INTERFACE**
Admin interface set up with details:
    email - wanjirumugo@gmail.com
    username - Wanjiru
    password - 123456
Data seeding from admin interface
Customise admin interface models:
    Plan - filter by insurance company
    Benefit - filter and search by name
    VetClinic - filter and search by address and name
    ExclusiveOf - fiiter by name

**SETUP SERIALIZERS FOR MODELS**
**InsuranceCompanySerializer**: a representation of each insurance company including their related plans.
**PlanSerializer**: a representation of each plan, including nested representation of related benefits, exclusions, and vetclinic service. 
    **Custome Validation Value**:
        For data integrity, a 400Error will be raised should the premium value be greater than the annual limit. 
**BenefitSerializer**: a representation of each benefit and its description
**ExclusiveOfSerializer**: a representation of each exclusion and its description
**VetClinicSerializer**: a representation of each vet clinic, its location, and contact phone

**STATIC FILES**
The following files were compiled in the static directory:
    scripts.js
    styles.css
    base.html


