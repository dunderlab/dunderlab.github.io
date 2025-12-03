# from radiant.framework.server import RadiantAPI, RadiantServer, render
# from radiant.framework import html, icons, select

from radiant.framework.server import RadiantInterfaceApp
from radiant.framework import html, icons, select


from browser import window, bind, document
from browser.template import Template

from projects import projects


########################################################################
class StaticApp(RadiantInterfaceApp):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        self.add_css_file('static/normalize.css')
        self.add_css_file('static/styles.css')
        self.add_css_file('static/backgrounds.css')

        self.last_scroll_position = 0
        self.is_auto_scrolling = False

        self.build_menubar()
        self.body <= self.build_portrait()
        self.body <= self.build_capabilities()
        self.body <= self.build_mission_and_vision()
        self.body <= self.build_projects_and_development()
        self.body <= self.build_clients()
        self.body <= self.build_contact()
        self.body <= self.build_footer()

        for anchor in document.select('a[href^="#"]'):
            anchor.bind('click', self.smooth_scroll)

        window.bind('scrollend', self.adjust_scroll)
        window.bind('scroll', self.cambiar_estilo)
        window.bind('scroll', self.on_scroll)

    # ----------------------------------------------------------------------
    def on_scroll(self, event):
        scrollTop = window.pageYOffset or document.documentElement.scrollTop
        document.select_one('#dunderlab--container-home').style.backgroundPositionY = str(scrollTop * 0.5) + 'px'

    # ----------------------------------------------------------------------
    def build_menubar(self):
        """"""
        self.menubar = html.DIV(id='dunderlab--menubar')
        self.menubar <= html.DIV('', Class='dunderlab--home')

        menu = [
            'Home',
            'Competencies',
            'Mission & Vision',
            'Projects & Developments',
            'Clients',
            'Contact',
        ]

        with html.DIV(Class='dunderlab-toolbar-menu').context(self.menubar) as parent:
            with html.UL(Class='dunderlab-menu').context as menubar_parent:
                for element in menu:
                    element_id = element.lower().replace(" ", "_").replace("&", "and")
                    li = html.LI(Class='dunderlab-menu--item', id=f'{element_id}--menu')
                    if element == 'Home':
                        li.classes.append('selected')
                    li <= html.A(f'{element}', href=f'#{element_id}')
                    li <= html.SPAN('', Class='dunderlab--cursor')
                    menubar_parent <= li

        self.menubar <= html.DIV(Class='dunderlab-float-menu--launcher', style={'background-image': 'url(/root/assets/icons/tally-4.svg)'})

        with html.DIV(Class='dunderlab-float-menu', style={'display': 'none', }).context(self.body) as parent:
            with html.UL(Class='dunderlab-menu').context as menubar_parent:
                for element in menu:
                    element_id = element.lower().replace(" ", "_").replace("&", "and")
                    li = html.LI(Class='dunderlab-menu--item', id=f'{element_id}--menu')
                    if element == 'Home':
                        li.classes.append('selected')
                    li <= html.A(f'{element}', href=f'#{element_id}')
                    li <= html.SPAN('', Class='dunderlab--cursor')
                    menubar_parent <= li

        self.body <= self.menubar
        select('.dunderlab-float-menu--launcher').bind('click', self.toggle('.dunderlab-float-menu'))
        select('.dunderlab-menu--item').bind('click', self.hide('.dunderlab-float-menu'))

    # ----------------------------------------------------------------------
    def cambiar_estilo(self, evt):
        """"""
        if window.scrollY < 600:
            # self.menubar.style = {'background-color': f'rgba(26, 83, 92, {self.map_value(window.scrollY, 0, 600, 0, 0.2)})', }
            document.select_one('.dunderlab--home').style = {'background-size': f'{self.map_value(window.scrollY, 0, 600, 215, 140)}px', }
        else:
            # self.menubar.style = {'background-color': f'rgba(26, 83, 92, 0.2)', }
            document.select_one('.dunderlab--home').style = {'background-size': f'140px', }

    # ----------------------------------------------------------------------
    def smooth_scroll(self, evt):
        """"""
        evt.preventDefault()
        target_id = evt.target.href.split('#')[-1]
        target_element = document.select_one(f'#dunderlab--container-{target_id}')
        select('.dunderlab-menu--item').classes.remove('selected')
        select(f'#{target_id}--menu').classes.append('selected')

        window.scroll({
            'top': target_element.offsetTop - 90,
            'left': 0,
            'behavior': 'smooth'
        })
        self.is_auto_scrolling = True
        window.setTimeout(lambda: setattr(self, 'is_auto_scrolling', False), 1000)

    # ----------------------------------------------------------------------
    def adjust_scroll(self, event):
        """"""
        if self.is_auto_scrolling:
            return

        sections = document.select('.dunderlab--container')  # Ajusta el selector según sea necesario
        current_scroll_position = window.scrollY

        # Determinar la dirección del scroll
        scrolling_down = current_scroll_position > self.last_scroll_position
        self.last_scroll_position = current_scroll_position

        closest_section = None
        minimum_distance = float('inf')

        for section in sections:
            section_position = section.offsetTop
            distance = section_position - current_scroll_position

            if scrolling_down and distance > 0 and distance < minimum_distance:
                # Scroll hacia abajo, selecciona la próxima sección
                closest_section = section
                minimum_distance = distance
                select('.dunderlab-menu--item').classes.remove('selected')
                select(f'#{section.id.replace("dunderlab--container-",  "")}--menu').classes.append('selected')

            elif not scrolling_down and distance < 0 and abs(distance) < minimum_distance:
                # Scroll hacia arriba, selecciona la sección anterior
                closest_section = section
                minimum_distance = abs(distance)
                select('.dunderlab-menu--item').classes.remove('selected')
                select(f'#{section.id.replace("dunderlab--container-",  "")}--menu').classes.append('selected')

        if closest_section and minimum_distance < 700:
            window.scrollTo({
                'top': closest_section.offsetTop - 90,
                'behavior': 'smooth'
            })
        window.setTimeout(lambda: setattr(self, 'is_auto_scrolling', False), 500)
        self.is_auto_scrolling = True

    # ----------------------------------------------------------------------
    def build_portrait(self):
        """"""
        with html.DIV(Class='dunderlab--container container-fluid', id='dunderlab--container-home').context as container:
            with html.DIV(Class='row').context as row:
                with html.DIV(Class='col-12 col-lg-6 dunderlab-home').context as col:
                    col <= html.H2('Fueling Innovation with Open Source: Advancing Technological Frontiers.', Class='dunderlab-contrast_text')
                    col.style['padding-top'] = '30vh'
                with html.DIV(Class='col').context as col:
                    col <= html.H1('')

        return container

    # ----------------------------------------------------------------------
    def build_capabilities(self):
        """"""
        cards_style = 'col-sm-12 col-md-6 col-lg-4'
        with html.DIV(Class='dunderlab--container container', id='dunderlab--container-competencies').context as container:
            with html.DIV(Class='row').context as row:

                with html.DIV(Class=cards_style).context:
                    with html.DIV(Class='dunderlab-capability').context as col:
                        col <= html.DIV(style={'background-image': 'url(/root/assets/icons/laptop-code.svg)'}, Class='dunderlab-capability--image')
                        col <= html.H1('Open-Source Software Development')
                        col <= html.DIV('Developing versatile and community-driven open-source software solutions.', Class='dunderlab-capability--description', )

                with html.DIV(Class=cards_style).context:
                    with html.DIV(Class='dunderlab-capability').context as col:
                        col <= html.DIV(style={'background-image': 'url(/root/assets/icons/lightbulb-setting.svg)'}, Class='dunderlab-capability--image')
                        col <= html.H1('Innovative Prototyping Design')
                        col <= html.DIV('Crafting functional prototypes with a focus on IoT and smart technologies.', Class='dunderlab-capability--description', )

                with html.DIV(Class=cards_style).context:
                    with html.DIV(Class='dunderlab-capability').context as col:
                        col <= html.DIV(style={'background-image': 'url(/root/assets/icons/microchip.svg)'}, Class='dunderlab-capability--image')
                        col <= html.H1('Embedded Systems and IoT Development')
                        col <= html.DIV('Creating intelligent, interconnected systems for a wide range of applications.', Class='dunderlab-capability--description', )

            # with html.DIV(Class='row', style={'margin-top': '90px'}).context as row:

                with html.DIV(Class=cards_style).context:
                    with html.DIV(Class='dunderlab-capability').context as col:
                        col <= html.DIV(style={'background-image': 'url(/root/assets/icons/rocket-lunch.svg)'}, Class='dunderlab-capability--image')
                        col <= html.H1('Library Development for Specialized Applications')
                        col <= html.DIV('Building efficient, custom software libraries for specific tech needs.', Class='dunderlab-capability--description', )

                with html.DIV(Class=cards_style).context:
                    with html.DIV(Class='dunderlab-capability').context as col:
                        col <= html.DIV(style={'background-image': 'url(/root/assets/icons/cloud-code.svg)'}, Class='dunderlab-capability--image')
                        col <= html.H1('Cloud Computing and Infrastructure')
                        col <= html.DIV('Providing scalable and secure cloud-based solutions, optimizing data storage, processing, and accessibility for diverse applications.', Class='dunderlab-capability--description', )

                with html.DIV(Class=cards_style).context:
                    with html.DIV(Class='dunderlab-capability').context as col:
                        col <= html.DIV(style={'background-image': 'url(/root/assets/icons/brain-circuit.svg)'}, Class='dunderlab-capability--image')
                        col <= html.H1('Advanced Digital Signal Processing Solutions')
                        col <= html.DIV('Delivering high-performance signal processing in telecommunications and beyond.', Class='dunderlab-capability--description', )

        return container

    # ----------------------------------------------------------------------
    def build_mission_and_vision(self):
        """"""
        with html.DIV(Class='dunderlab--container container', id='dunderlab--container-mission_and_vision').context as container:
            with html.DIV(Class='row').context as row:

                with html.DIV(Class='col-12 dunderlab-mav').context as col:
                    col <= html.H1('Mission')
                    col <= html.DIV('DunderLab is committed to innovating in the realms of software and hardware development, upholding the principles of free and open-source software and hardware. Our focus is on crafting high-quality, accessible, and customizable technological solutions tailored to meet the specific needs of our clients. We strive to propel technological advancement through the creation of unique hardware and prototypes, always maintaining an unwavering commitment to freedom, innovation, and technological sustainability.')

                row <= html.HR(style={'margin-top': '10vh', 'width': '50vw'})

                with html.DIV(Class='col-12 dunderlab-mav').context as col:
                    col <= html.H1('Vision', style={'text-align': 'right', })
                    col <= html.DIV('Our vision at DunderLab is to be globally recognized leaders in the development of free and open-source software and hardware. We aspire to transform and enrich the technology industry through innovative solution design and the promotion of open-source culture. We envision ourselves as a company that makes a difference in the tech field, inspiring other organizations to adopt more open, collaborative, and ethical practices in technology development.',
                                    style={'text-align': 'right', })

        return container

    # ----------------------------------------------------------------------
    def build_projects_and_development(self):
        """"""
        with html.DIV(Class='dunderlab--container container', id='dunderlab--container-projects_and_developments').context as container:
            container <= html.H1('Projects & Developments', Class='dunderlab--container-title')
            with html.DIV(Class='row').context as row:

                for i, project in enumerate(sorted(projects, key=lambda x: x['year'], reverse=True)):

                    if i % 2 == 0:
                        style = 'dunderlab-dev--align-right'
                        style_tools = 'dunderlab-dev--tools--even'
                        frame_style = 'dunderlab-dev--even'
                        logo_style = 'dunderlab-dev--logo-even'

                    else:
                        style = ''
                        style_tools = ''
                        frame_style = ''
                        logo_style = 'dunderlab-dev--logo-odd'

                    with html.DIV(Class=f'col-12 col-md-6 dunderlab-dev {frame_style}').context as col:
                        with html.DIV(Class='row').context as row:

                            with html.DIV(Class=f'dunderlab-dev--logo dunderlab-dev--logo-pre {logo_style} col-auto').context as col_logo:
                                col_logo.style['background-image'] = f"url({project['logo']})"

                            with html.DIV(Class=f'col').context as col_head:
                                col_head <= html.H1(project['name'], Class=style)
                                col_head <= html.H2(project['type'], Class=style)

                            with html.DIV(Class=f'dunderlab-dev--logo dunderlab-dev--logo-post {logo_style} col-auto').context as col_logo:
                                col_logo.style['background-image'] = f"url({project['logo']})"

                        col <= html.DIV(project['description'], Class=style)

                        with html.DIV(Class=f'dunderlab-line {style}').context(col) as line:
                            if project.get('documentation'):
                                line <= icons.fa('book', Class=f'dunderlab-dev--fa-icon dunderlab-dev--logo-pre {logo_style}')
                                line <= html.A(project['documentation'], href=project['documentation'], Class=style)
                                line <= icons.fa('book', Class=f'dunderlab-dev--fa-icon dunderlab-dev--logo-post {logo_style}')

                        with html.DIV(Class=f'dunderlab-line {style}').context(col) as line:
                            if project.get('repository'):
                                line <= icons.fa('github', mode='brands', Class=f'dunderlab-dev--fa-icon dunderlab-dev--logo-pre {logo_style}')
                                line <= html.A(project['repository'], href=project['repository'], Class=style)
                                line <= icons.fa('github', mode='brands', Class=f'dunderlab-dev--fa-icon dunderlab-dev--logo-post {logo_style}')

                        with html.DIV(Class=f'dunderlab-line {style}').context(col) as line:
                            if project.get('page'):
                                line <= icons.fa('link', Class=f'dunderlab-dev--fa-icon dunderlab-dev--logo-pre {logo_style}')
                                line <= html.A(project['page'], href=project['page'], Class=style)
                                line <= icons.fa('link', Class=f'dunderlab-dev--fa-icon dunderlab-dev--logo-post {logo_style}')

                        col <= html.DIV(', '.join(project['tools']), Class=f'dunderlab-dev--tools {style_tools}')

                    with html.DIV(Class='col-6').context:
                        pass
                    with html.DIV(Class='col-6').context:
                        pass

        return container

    # ----------------------------------------------------------------------
    def build_clients(self):
        """"""
        with html.DIV(Class='dunderlab--container container', id='dunderlab--container-clients').context as container:
            container <= html.H1('University Partnerships and Supply', Class='dunderlab--container-title')
            with html.DIV(Class='row', style={'margin-top': '100px'}).context as row:

                with html.DIV(Class='col dunderlab-client').context as col:
                    col.style['background-image'] = 'url(/root/assets/clients/Logotipo_de_la_Universidad_Nacional_de_Colombia.svg)'

                with html.DIV(Class='col dunderlab-client').context as col:
                    col.style['background-image'] = 'url(/root/assets/clients/utp_universidad_tecnologica_de_pereira.svg)'

                with html.DIV(Class='col dunderlab-client').context as col:
                    col.style['background-image'] = 'url(/root/assets/clients/Logo_de_la_Universidad_de_Caldas.svg)'

        return container

    # ----------------------------------------------------------------------
    def build_contact(self):
        """"""
        with html.DIV(Class='dunderlab--container container', id='dunderlab--container-contact').context as container:
            container <= html.H1('Contact', Class='dunderlab--container-title')
            with html.DIV(Class='row').context as row:
                with html.DIV(Class='col').context as col:

                    with html.DIV(Class='dunderlab-line').context as line:
                        line <= icons.fa('envelope')
                        line <= html.SPAN('contact [at] dunderlab.com')

                    with html.DIV(Class='dunderlab-line').context as line:
                        line <= icons.fa('phone')
                        line <= html.SPAN('(+57) 314 370 5156')

                    with html.DIV(Class='dunderlab-line').context as line:
                        line <= icons.fa('map-location-dot')
                        line <= html.SPAN('Eje Cafetero, Colombia')

        return container

    # ----------------------------------------------------------------------

    def build_footer(self):
        """"""
        with html.DIV(Class='dunderlab--container container-fluid', id='dunderlab--container-footer').context as container:
            with html.DIV(Class='row').context as row:
                with html.DIV(Class='col', style={'text-align': 'center', }).context as col:

                    col <= html.SPAN('Made with ')
                    col <= icons.fa('heart', mode='regular', style={'color': 'var(--link-color)', })
                    col <= html.SPAN(' by DunderLab (obviously)')
                    col <= html.BR()
                    col <= html.SPAN('This site has been built using ')
                    col <= html.A('Radiant Framework', href='https://radiant-framework.readthedocs.io/')
                    col <= html.SPAN(' technology')
                    col <= html.BR()
                    col <= html.SPAN('© 2025. Some rights reserved under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)')

        return container


if __name__ == '__main__':
    StaticApp(#'StaticApp',
                  host='0.0.0.0',
                  port='5050',
                  template='layout.html',
                  static_app='docs',
                  modules=['roboto', 'fontawesome'],
                  page_title='__lab__',
                  page_description='Fueling Innovation with Open Source: Advancing Technological Frontiers.',
                  page_image='https://www.dunderlab.com/root/assets/logo_render_dark.svg',
                  page_url='dunderlab.com',
                  page_summary_large_image='https://www.dunderlab.com/root/assets/logo_render_dark.svg',
                  page_site='@yeisondev',
                  page_author='Yeison Cardona',
                  page_copyright='',
                  ).serve()
