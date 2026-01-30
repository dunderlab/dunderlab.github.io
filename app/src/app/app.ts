import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {EmptyLayoutComponent} from './shared/layouts/empty/empty.component';
import {ThemeService} from './shared/services/theme/theme.service';
import {MatIconRegistry} from '@angular/material/icon';
import {EmptyLayoutService} from './shared/layouts/empty/empty.service';
import {NavBarService} from './shared/components/navbar/navbar.service';
import {HomeComponent} from './core/home/home.component';
import {SkillsComponent} from './core/skills/skills.component';
import {MissionVisionComponent} from './core/mission_vision/mission_vision.component';
import {ProjectsComponent} from './core/projects/projects.component';
import {ClientsComponent} from './core/clients/clients.component';
import {ContactComponent} from './core/contact/contact.component';

@Component({
  selector: 'app-root',
  imports: [
    EmptyLayoutComponent,
    HomeComponent,
    SkillsComponent,
    MissionVisionComponent,
    ProjectsComponent,
    ClientsComponent,
    ContactComponent,
  ],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

  constructor(
    public themeService: ThemeService,
    public emptyLayoutService: EmptyLayoutService,
    public navbarService: NavBarService,
    iconRegistry: MatIconRegistry,

    ){

    emptyLayoutService.brand.set(true);

    themeService.applyMaterialThemeFromColor('#006a69', "html", themeService.mode(), 26, 87);
    iconRegistry.setDefaultFontSetClass('material-symbols-sharp');

  }

  ngAfterViewInit() {
    this.navbarService.setNavActiveLink('home', 'Inicio');
  }




}
