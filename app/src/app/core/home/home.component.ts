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
      "Impulsando la Innovación con Código Abierto: Avanzando Fronteras Tecnológicas."
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
