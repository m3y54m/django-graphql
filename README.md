# Django GraphQL API

Written based on this tutorial:

https://tech.sahab.ir/%D8%B3%D8%A7%D8%AE%D8%AA-api-%D9%85%D8%AF%D8%B1%D9%86-%D8%A8%D8%A7-graphql-%D8%A8%D8%AE%D8%B4-%D8%AF%D9%88%D9%85-ewxcofo288mz


Commands used since the start of project:

## Initialize Django project

```console
cd django-graphql
django-admin startproject backend_api_project .

```

## Setting Up the GraphQL

Install the `graphene-django` package:

```console
pip install graphene-django

```

### Start a new application called `graphql_app`

```console
python manage.py startapp graphql_app

```

### Generate the GraphQL schema file 

```console
python manage.py graphql_schema --out schema.graphql

```
