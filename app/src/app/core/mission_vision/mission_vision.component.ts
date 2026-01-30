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
    en: '',
    es: 'DunderLab está comprometido con la innovación en los campos del desarrollo de software y hardware, defendiendo los principios del software y hardware libre y de código abierto. Nos enfocamos en crear soluciones tecnológicas de alta calidad, accesibles y personalizables, adaptadas para satisfacer las necesidades específicas de nuestros clientes. Nos esforzamos por impulsar el avance tecnológico mediante la creación de hardware y prototipos únicos, manteniendo siempre un compromiso inquebrantable con la libertad, la innovación y la sostenibilidad tecnológica.'
  }

  vision = {
    en: '',
    es: 'Nuestra visión en DunderLab es ser líderes globalmente reconocidos en el desarrollo de software y hardware libre y de código abierto. Aspiramos a transformar y enriquecer la industria tecnológica a través del diseño de soluciones innovadoras y la promoción de la cultura del código abierto. Nos visualizamos como una empresa que marca la diferencia en el campo tecnológico, inspirando a otras organizaciones a adoptar prácticas más abiertas, colaborativas y éticas en el desarrollo tecnológico.'
  }

}
