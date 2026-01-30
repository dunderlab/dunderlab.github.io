import {Component, computed, signal, HostListener} from '@angular/core';
import { CommonModule } from '@angular/common';
import {ContainerComponent} from '../container/container.component';
import {ThemeService} from '../../shared/services/theme/theme.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    ContainerComponent
  ],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  backgroundPositionY = signal('-30px');

  tagline = computed(() => {
    const taglines = [
      "Diseñamos tecnología que resuelve problemas reales.",
      "Ingeniería de software y hardware sin atajos.",
      "Convertimos complejidad en soluciones simples.",
      "Arquitectura sólida. Resultados medibles.",
      "Menos promesas. Más sistemas funcionando.",
      "Tecnología confiable, desde el diseño hasta producción."
    ];
    return taglines[Math.floor(Math.random() * taglines.length)];
  });


  constructor(
    public themeService: ThemeService,
    ) {}

  @HostListener('window:scroll')
  onScroll(): void {
    const scrollTop =
      window.pageYOffset || document.documentElement.scrollTop || 0;

    // parallax factor (0.5 = slower than scroll)
    const y = scrollTop * 0.5;

    this.backgroundPositionY.set(`${-30 + y}px`);
  }

}
