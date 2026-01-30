import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ContainerComponent} from '../container/container.component';

@Component({
  selector: 'app-mission-vision',
  standalone: true,
  imports: [CommonModule, ContainerComponent],
  templateUrl: './mission_vision.component.html',
  styleUrls: ['./mission_vision.component.scss']
})
export class MissionVisionComponent {



  mission = {
    en: 'We design, build and deploy reliable software and hardware systems that solve real operational problems. Through rigorous engineering, careful architecture and measurable outcomes, we deliver technology that is robust, scalable and ready for production environments.',
    es: 'Diseñamos, construimos e implementamos sistemas de software y hardware confiables que resuelven problemas operativos reales. Aplicamos ingeniería rigurosa, arquitectura sólida y métricas verificables para entregar tecnología robusta, escalable y lista para entornos de producción.'
  }

  vision = {
    en: 'To become a leading engineering company recognized for transforming complex challenges into practical and sustainable technological solutions. We aim to be a trusted partner for organizations that require precision, reliability and long-term impact from their technology investments.',
    es: 'Ser una empresa de ingeniería líder, reconocida por transformar desafíos complejos en soluciones tecnológicas prácticas y sostenibles. Aspiramos a convertirnos en un socio estratégico de confianza para organizaciones que exigen precisión, confiabilidad e impacto a largo plazo en sus inversiones tecnológicas.'
  }

}
