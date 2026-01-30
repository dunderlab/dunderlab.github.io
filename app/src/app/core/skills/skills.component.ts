import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ContainerComponent} from '../container/container.component';
import {MatCardModule} from '@angular/material/card';
import {MatIconModule} from '@angular/material/icon';


@Component({
  selector: 'app-skills',
  standalone: true,
  imports: [CommonModule, ContainerComponent, MatCardModule, MatIconModule],
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.scss']
})
export class SkillsComponent {


  skills = [
    {
      title: {
        es: 'Desarrollo de Software de Código Abierto',
        en: 'Open-Source Software Development'
      },
      description: {
        es: 'Desarrollando soluciones de software de código abierto versátiles e impulsadas por la comunidad.',
        en: 'Developing versatile and community-driven open-source software solutions.'
      },
      icon: 'code'
    },
    {
      title: {
        es: 'Diseño de Prototipos Innovadores',
        en: 'Innovative Prototyping Design'
      },
      description: {
        es: 'Creación de prototipos funcionales enfocados en IoT y tecnologías inteligentes.',
        en: 'Crafting functional prototypes with a focus on IoT and smart technologies.'
      },
      icon: 'science'
    },
    {
      title: {
        es: 'Desarrollo de Sistemas Embebidos e IoT',
        en: 'Embedded Systems and IoT Development'
      },
      description: {
        es: 'Creación de sistemas inteligentes e interconectados para una amplia gama de aplicaciones.',
        en: 'Creating intelligent, interconnected systems for a wide range of applications.'
      },
      icon: 'developer_board'
    },
    {
      title: {
        es: 'Desarrollo de Bibliotecas para Aplicaciones Especializadas',
        en: 'Library Development for Specialized Applications'
      },
      description: {
        es: 'Construcción de bibliotecas de software eficientes y personalizadas para necesidades técnicas específicas.',
        en: 'Building efficient, custom software libraries for specific tech needs.'
      },
      icon: 'widgets'
    },
    {
      title: {
        es: 'Computación en la Nube e Infraestructura',
        en: 'Cloud Computing and Infrastructure'
      },
      description: {
        es: 'Proporcionando soluciones escalables y seguras basadas en la nube, optimizando el almacenamiento, procesamiento y accesibilidad de datos para diversas aplicaciones.',
        en: 'Providing scalable and secure cloud-based solutions, optimizing data storage, processing, and accessibility for diverse applications.'
      },
      icon: 'backup'
    },
    {
      title: {
        es: 'Soluciones Avanzadas de Procesamiento de Señales Digitales',
        en: 'Advanced Digital Signal Processing Solutions'
      },
      description: {
        es: 'Entregando procesamiento de señales de alto rendimiento en telecomunicaciones y más allá.',
        en: 'Delivering high-performance signal processing in telecommunications and beyond.'
      },
      icon: 'flowchart'
    }
  ];



}
