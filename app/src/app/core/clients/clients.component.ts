import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ContainerComponent} from "../container/container.component";
import {ThemeService} from '../../shared/services/theme/theme.service';

@Component({
  selector: 'app-clients',
  standalone: true,
    imports: [CommonModule, ContainerComponent],
  templateUrl: './clients.component.html',
  styleUrls: ['./clients.component.scss']
})
export class ClientsComponent {

  constructor(public themeService: ThemeService) { }

  clients = {
    logos: [
      '/assets/images/clients/Logo_de_la_Universidad_de_Caldas.svg',
      '/assets/images/clients/Logotipo_de_la_Universidad_Nacional_de_Colombia.svg',
      '/assets/images/clients/utp_universidad_tecnologica_de_pereira.svg',
    ],
    title: {
      en: '',
      es: 'Colaboraciones institucionales',
    },
    about: {
      en: 'Organizations that contracted our engineering, R&D, and specialized technology services.',
      es: 'Organizaciones que contrataron nuestros servicios de ingeniería, I+D y provisión de tecnología especializada.'
    }
  }


  mentors = {
    logos: [
      '/assets/images/support/logo-cientech.png',
      '/assets/images/support/Logo_innpulsa_color.png',
    ],
    title: {
      en: '',
      es: 'Apoyo al crecimiento'
    },
    about: {
      en: 'Organizations that provided mentorship, incubation, and strategic support for growth.',
      es: 'Organizaciones que brindaron mentoría, acompañamiento estratégico e impulso al crecimiento de nuestros proyectos.'
    }
  }


}
