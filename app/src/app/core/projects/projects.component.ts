import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ContainerComponent} from "../container/container.component";
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatChipsModule} from '@angular/material/chips';


@Component({
  selector: 'app-projects',
  standalone: true,
  imports: [CommonModule, ContainerComponent, MatCardModule, MatButtonModule, MatIconModule, MatChipsModule],
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.scss']
})
export class ProjectsComponent {


  projects = [
    {
      "name": "BCI Framework",
      "type": {"en": "Desktop application", "es": "Aplicación de escritorio"},
      "description": {
        "en": "A distributed processing tool, stimuli delivery, psychophysiological experiments designer and real-time data visualizations for OpenBCI.",
        "es": "Una herramienta de procesamiento distribuido, entrega de estímulos, diseño de experimentos psicofisiológicos y visualización de datos en tiempo real para OpenBCI."
      },
      "tools": ["Python", "PySide", "OpenBCI", "Kafka", "GNU/Linux"],
      "documentation": "https://bci-framework.readthedocs.io",
      "repository": "https://github.com/dunderlab/bci-framework",
      "logo": "https://bci-framework.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2021",
    },
    {
      "name": "OpenBCI Stream",
      "type": {"en": "Hardware drivers", "es": "Controladores de hardware"},
      "description": {
        "en": "High level Python module for EEG/EMG/ECG acquisition and distributed streaming for OpenBCI Cyton board.",
        "es": "Módulo Python de alto nivel para adquisición de EEG/EMG/ECG y transmisión distribuida para la tarjeta OpenBCI Cyton."
      },
      "tools": ["Python", "OpenBCI", "Kafka", "GNU/Linux", "Raspberry Pi"],
      "documentation": "https://openbci-stream.readthedocs.io/",
      "repository": "https://github.com/dunderlab/openbci-stream",
      "logo": "https://openbci-stream.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2019",
    },
    {
      "name": "Qt Material",
      "type": {"en": "GUI theme", "es": "Tema gráfico"},
      "description": {
        "en": "This is another stylesheet for PySide6, PySide2, PyQt5 and PyQt6, which looks like Material Design (close enough).",
        "es": "Otro conjunto de estilos para PySide6, PySide2, PyQt5 y PyQt6, con aspecto similar a Material Design."
      },
      "tools": ["Python", "OpenBCI", "Kafka", "GNU/Linux", "Raspberry Pi"],
      "documentation": "https://qt-material.readthedocs.io/",
      "repository": "https://github.com/dunderlab/qt-material",
      "logo": "https://qt-material.readthedocs.io/en/latest/_static/logo.png",
      "year": "2019",
    },
    {
      "name": "Radiant Framework",
      "type": {"en": "Web apps development framework", "es": "Framework para desarrollo de aplicaciones web"},
      "description": {
        "en": "A novel web framework designed to leverage the capabilities of Brython, allowing developers to write web applications entirely in Python without requiring HTML, CSS or JavaScript.",
        "es": "Un novedoso framework web basado en Brython que permite escribir aplicaciones web completamente en Python, sin necesidad de HTML, CSS o JavaScript."
      },
      "tools": ["Python", "Brython", "Tornado"],
      "documentation": "https://radiant-framework.readthedocs.io",
      "repository": "https://github.com/dunderlab/python-radiant_framework",
      "logo": "https://radiant-framework.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2023",
    },
    {
      "name": "Radiant Compiler",
      "type": {"en": "Android APK generator", "es": "Generador de APKs para Android"},
      "description": {
        "en": "Tool for compiling Brython and Django applications into Android APK packages.",
        "es": "Herramienta para compilar aplicaciones Brython y Django en paquetes APK para Android."
      },
      "tools": ["Python", "Python-for-Android", "Django", "Android", "Docker"],
      "documentation": "https://radiant-compiler.readthedocs.io/",
      "repository": "https://github.com/dunderlab/python-radiant_compiler",
      "logo": "https://radiant-compiler.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2023",
    },
    {
      "name": "DunderLab’s Documentation Guide",
      "type": {"en": "Python module", "es": "Módulo de Python"},
      "description": {
        "en": "Facilitates building Sphinx documentation directly from Jupyter Notebooks using a preconfigured nbsphinx environment.",
        "es": "Facilita la creación de documentación Sphinx directamente desde notebooks de Jupyter utilizando un entorno nbsphinx preconfigurado."
      },
      "tools": ["Python", "Sphinx"],
      "documentation": "https://dunderlab-docs.readthedocs.io/",
      "repository": "https://github.com/dunderlab/python-dunderlab.docs",
      "logo": "https://dunderlab-docs.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2023",
    },
    {
      "name": "TimeScaleDB App",
      "type": {"en": "Django application", "es": "Aplicación Django"},
      "description": {
        "en": "Django API for managing and querying time-series data using PostgreSQL and TimeScaleDB.",
        "es": "API en Django para gestionar y consultar datos de series temporales usando PostgreSQL y TimeScaleDB."
      },
      "tools": ["Python", "Django", "TimeScaleDB", "PostgreSQL"],
      "documentation": "https://timescaledb-app.readthedocs.io/",
      "repository": "https://github.com/dunderlab/python-django-timescaledbapp",
      "logo": "https://timescaledb-app.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2023",
    },
    {
      "name": "CtenoLab",
      "type": {"en": "Web application", "es": "Aplicación web"},
      "description": {
        "en": "Runs EEG and BCI paradigms directly in the browser with real-time synchronization using WebUSB/WebSerial.",
        "es": "Ejecuta paradigmas EEG y BCI directamente en el navegador con sincronización en tiempo real usando WebUSB/WebSerial."
      },
      "tools": ["Angular", "WebUSB", "WebSerial"],
      "documentation": "",
      "repository": "",
      "logo": "https://cteno.dunderlab.com/assets/images/branding/app_logo_light.svg",
      "page": "https://ctenolab.com",
      "year": "2025",
    },
    {
      "name": "Chaski Confluent",
      "type": {"en": "Python module", "es": "Módulo de Python"},
      "description": {
        "en": "Asynchronous messaging, node discovery and remote method invocation for distributed systems.",
        "es": "Mensajería asíncrona, descubrimiento de nodos e invocación remota de métodos para sistemas distribuidos."
      },
      "tools": ["Python"],
      "documentation": "https://chaski-confluent.readthedocs.io/en/latest/",
      "repository": "https://github.com/dunderlab/python-chaski",
      "logo": "https://chaski-confluent.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2024",
    },
    {
      "name": "Dunderlab - visualizations",
      "type": {"en": "Python module", "es": "Módulo de Python"},
      "description": {
        "en": "Brain connectivity visualization, topoplots and EEG processing tools built with Matplotlib and MNE.",
        "es": "Herramientas para visualización de conectividad cerebral, topoplots y procesamiento EEG con Matplotlib y MNE."
      },
      "tools": ["Python", "Matplotlib", "NumPy", "Flask"],
      "documentation": "https://dunderlab.readthedocs.io/projects/Visualizations/en/latest/",
      "repository": "https://github.com/dunderlab/python-dunderlab.visualizations",
      "logo": "https://dunderlab.readthedocs.io/projects/Visualizations/en/latest/_images/conn.png",
      "year": "2019",
    },
    {
      "name": "Foundation",
      "type": {"en": "Python module", "es": "Módulo de Python"},
      "description": {
        "en": "Utilities for managing Docker-based workers with a Radiant web interface.",
        "es": "Utilidades para gestionar workers basados en Docker con una interfaz web Radiant."
      },
      "tools": ["Python", "Docker", "Django", "PostgreSQL"],
      "documentation": "",
      "repository": "https://github.com/dunderlab/python-dunderlab.foundation",
      "logo": "https://dunderlab-foundation.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2019",
    },
    {
      "name": "Matplotlib-FigureStream",
      "type": {"en": "Python module", "es": "Módulo de Python"},
      "description": {
        "en": "Backend for serving Matplotlib animations as real-time JPEG streams through Flask.",
        "es": "Backend para servir animaciones de Matplotlib como flujos JPEG en tiempo real usando Flask."
      },
      "tools": ["Python", "Matplotlib", "NumPy", "Flask"],
      "documentation": "https://figurestream.readthedocs.io/en/latest/",
      "repository": "https://github.com/dunderlab/python-matplotlib-figurestream",
      "logo": "https://figurestream.readthedocs.io/en/latest/_static/logo.svg",
      "year": "2019",
    },
  ]


  protected readonly print = print;
}
