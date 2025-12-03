projects = (
    {
        'name': 'BCI Framework',
        'type': 'Desktop application',
        'description': 'A distributed processing tool, stimuli delivery, psychophysiological experiments designer and real-time data visualizations for OpenBCI.',
        'tools': ['Python', 'PySide', 'OpenBCI', 'Kafka', 'GNU/Linux'],
        'documentation': 'https://bci-framework.readthedocs.io',
        'repository': 'https://github.com/dunderlab/bci-framework',
        'logo': 'https://bci-framework.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2021',
    },

    {
        'name': 'OpenBCI Stream',
        'type': 'Hardware drivers',
        'description': 'High level Python module for EEG/EMG/ECG acquisition and distributed streaming for OpenBCI Cyton board.',
        'tools': ['Python', 'OpenBCI', 'Kafka', 'GNU/Linux', 'Raspberry Pi'],
        'documentation': 'https://openbci-stream.readthedocs.io/',
        'repository': 'https://github.com/dunderlab/openbci-stream',
        'logo': 'https://openbci-stream.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2019',
    },

    {
        'name': 'Qt Material',
        'type': 'GUI theme',
        'description': 'This is another stylesheet for PySide6, PySide2, PyQt5 and PyQt6, which looks like Material Design (close enough).',
        'tools': ['Python', 'OpenBCI', 'Kafka', 'GNU/Linux', 'Raspberry Pi'],
        'documentation': 'https://qt-material.readthedocs.io/',
        'repository': 'https://github.com/dunderlab/qt-material',
        'logo': 'https://qt-material.readthedocs.io/en/latest/_static/logo.png',
        'year': '2019',
    },

    {
        'name': 'Radiant Framework',
        'type': 'Web apps development framework',
        'description': 'A novel web framework designed to leverage the capabilities of Brython, a browser-based Python implementation. This innovative approach allows developers to write web applications entirely in Python, bypassing the conventional requirements of HTML, CSS, or JavaScript for frontend development.',
        'tools': ['Python', 'Brython', 'Tornado'],
        'documentation': 'https://radiant-framework.readthedocs.io',
        'repository': 'https://github.com/dunderlab/python-radiant_framework',
        'logo': 'https://radiant-framework.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2023',
    },

    {
        'name': 'Radiant Compiler',
        'type': 'Android APK generator',
        'description': 'A tool designed for compiling Brighton and Django applications into Android packages (APKs), providing a streamlined and efficient process to convert these Python-based applications into a format that is compatible and installable on Android devices.',
        'tools': ['Python', 'Python-for-Android', 'Django', 'Android', 'Docker'],
        'documentation': 'https://radiant-compiler.readthedocs.io/',
        'repository': 'https://github.com/dunderlab/python-radiant_compiler',
        'logo': 'https://radiant-compiler.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2023',
    },

    {
        'name': 'DunderLab’s Documentation Guide',
        'type': 'Python module',
        'description': 'This Python module facilitates the creation of Sphinx Documentation directly from Jupyter Notebooks. Essentially, it provides a preconfigured environment that utilizes nbsphinx in the background, complete with custom styles and preloaded modules.',
        'tools': ['Python', 'Sphinx'],
        'documentation': 'https://dunderlab-docs.readthedocs.io/',
        'repository': 'https://github.com/dunderlab/python-dunderlab.docs',
        'logo': 'https://dunderlab-docs.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2023',
    },

    {
        'name': 'TimeScaleDB App',
        'type': 'Django application',
        'description': 'A Django-based web application that provides an API for managing and querying time-series data. This application utilizes RealTimeDB, a time-series database built atop PostgreSQL, for efficient storage and analysis of time-series data. With custom pagination classes and viewsets, the TimeScaleDB App delivers a powerful and flexible way to interact with Source, Measure, Channel, and TimeSerie models.',
        'tools': ['Python', 'Django', 'TimeScaleDB', 'PostgreSQL'],
        'documentation': 'https://timescaledb-app.readthedocs.io/',
        'repository': 'https://github.com/dunderlab/python-django-timescaledbapp',
        'logo': 'https://timescaledb-app.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2023',
    },

    # ============================
    # NUEVOS PROYECTOS UNIFICADOS
    # ============================

    {
        'name': 'CtenoLab',
        'type': 'Web application',
        'description': 'CtenoLab enables EEG and BCI paradigms directly in the browser with real-time hardware synchronization and WebUSB/WebSerial integration.',
        'tools': ['Angular', 'WebUSB', 'WebSerial'],
        'documentation': '',
        'repository': '',
        'logo': '/root/assets/images/cteno_logo.png',
        'page': 'https://ctenolab.com',
        'year': '2025',
    },

    {
        'name': 'Chaski Confluent',
        'type': 'Python module',
        'description': 'Asynchronous messaging, node discovery and remote method invocation for distributed systems.',
        'tools': ['Python'],
        'documentation': 'https://chaski-confluent.readthedocs.io/en/latest/',
        'repository': 'https://github.com/dunderlab/python-chaski',
        'logo': 'https://chaski-confluent.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2024',
    },

    {
        'name': 'Dunderlab - visualizations',
        'type': 'Python module',
        'description': 'Tools for brain connectivity visualization, topoplots and EEG processing (Matplotlib + MNE).',
        'tools': ['Python', 'Matplotlib', 'NumPy', 'Flask'],
        'documentation': 'https://dunderlab.readthedocs.io/projects/Visualizations/en/latest/',
        'repository': 'https://github.com/dunderlab/python-dunderlab.visualizations',
        'logo': 'https://dunderlab.readthedocs.io/projects/Visualizations/en/latest/_images/conn.png',
        'year': '2019',
    },

    {
        'name': 'Foundation',
        'type': '',
        'description': 'Utilities for managing Docker-based workers with a Radiant-based web interface.',
        'tools': ['Python', 'Docker', 'Django', 'PostgreSQL'],
        'documentation': '',
        'repository': 'https://github.com/dunderlab/python-dunderlab.foundation',
        'logo': 'https://dunderlab-foundation.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2019',
    },

    {
        'name': 'Matplotlib-FigureStream',
        'type': '',
        'description': 'Backend for serving Matplotlib animations as real-time JPEG streams through Flask.',
        'tools': ['Python', 'Matplotlib', 'NumPy', 'Flask'],
        'documentation': 'https://figurestream.readthedocs.io/en/latest/',
        'repository': 'https://github.com/dunderlab/python-matplotlib-figurestream',
        'logo': 'https://figurestream.readthedocs.io/en/latest/_static/logo.svg',
        'year': '2019',
    },

)
