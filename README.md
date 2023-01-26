# Django CRUD and Forms

## Author: Domaine Scully

## Overview

Add full CRUD functionality to Django project that allows Creating, Reading, Updating and Deleting.

## Feature Tasks and Requirements

- Create snacks_crud_project Django project
- Create snacks app
- Create Snack model
  - title field
  - purchaser field
  - description field
  - Register model with admin
- Create SnackListView that extends appropriate generic view
  - associated url path is an empty string
- Create SnackDetailView that extends appropriate generic view
  - associated url path is <int:pk>/
- Create SnackCreateView that extends appropriate generic view
  - associated url path is create/
- Create SnackUpdateView that extends appropriate generic view
  - associated url path is <int:pk>/update/
- Create SnackDeleteView that extends appropriate generic view
  - associated url path is <int:pk>/delete/
- Add urls to support all views, with appropriate names
- Add templates to support all views
- Add navigation links in appropriate locations to access all pages
- Make all necessary changes to project level files for project to run

## User Acceptance Tests

- Test all Views
- Test Model
  - string representation
  - all fields