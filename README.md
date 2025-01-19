# Title

A Comparative Analysis of Solar Energy Infrastructure and Electric Vehicle Adoption Patterns

# Description

The global shift toward sustainable energy solutions has placed solar energy and electric vehicles (EVs) to the forefront of modern energy regulations. In order to examine their interdependencies and offer useful information for energy planning in both urban and rural areas, this study looks into the adoption trends of solar energy installations and electric vehicle registrations. We find trends, correlations, and important factors influencing adoption in both urban and rural areas by examining two extensive datasets: data on solar energy installations and data on electric car registrations. The study finds that large-scale solar farms in rural areas and rooftop solar installations in urban areas have complementing connections with EV adoption. The recommendations for energy policies that close the gap between urban and rural areas and promote a cohesive, sustainable energy ecosystem are based on this investigation.

# Datasources

##  Solar Footprints Dataset (Dataset 1)

This dataset provides geospatial data on solar-powered electric generation facilities and related infrastructure in California, offering insights into renewable energy distribution in the state.

Source : https://opendatacommons.org/licenses/odbl/1-0/.

Data URL : https://cecgis-caenergy.opendata.arcgis.com/api/download/v1/items/9398e39a0424434b9e95ccf8e89

Data Type : CSV

## Electric Vehicle Population Data (Dataset 2)

This dataset tracks registered Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) in Washington, highlighting adoption patterns of clean energy consumption.

Source : http://opendatacommons.org/licenses/odbl/1.0/

Data URL : https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD

Data Type : CSV

# Overview

## Project Features

1.  Data Cleaning: The project includes data cleaning operations to handle issues such as duplicates, missing values, and inconsistencies in the dataset.

2.  SQLite Database: It utilizes an SQLite database to store and manage the cleaned and transformed data.

3.  Dataset Transformation: The project performs data transformation operations to prepare the dataset for analysis or further processing.

4.  Dataset Downloading: It can download datasets from external sources for analysis and integration into the project.

## Technologies used

Python, Sqlite

# License


This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
