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

  alliances= {

    alliances: [
    '/assets/images/clients/Logo_de_la_Universidad_de_Caldas.svg',
    '/assets/images/clients/Logotipo_de_la_Universidad_Nacional_de_Colombia.svg',
    '/assets/images/clients/utp_universidad_tecnologica_de_pereira.svg',
  ],
    title: {
      en: '',
      es: 'Colaboración en I+D y provisión de tecnología especializada.'
    },
    about: {
      en: '',
      es: 'Organizaciones con las que colaboramos en I+D, transferencia tecnológica y provisión de instrumentación y soluciones técnicas especializadas.'
    }


  }




}
