  <testApp>:
                Screen:

                    MDBottomNavigation:
                        #panel_color: "#eeeaea"
                        selected_color_background: "blue"
                        text_color_active: "lightgrey"

                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Login'
                            icon: 'account'

                            Image:
                                source: "img/sunset.jpg "
                                size_hint: None, None
                                width: "960dp"
                                height: "1440dp"
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                opacity: 0.5
                            Image:
                                source: "img/Ubraen.png "
                                size_hint: None, None
                                width: "80dp"
                                height: "80dp"
                                pos_hint: {'center_x': .5, 'center_y': .9}
                        
                            MDLabel:
                                text: "Ubraek"
                                color: "#F8F7F7"
                                bold: True
                                font_size: "48dp"
                                halign: "center"
                                pos_hint: {'center_y': .79}
                            MDLabel:
                                id: login_error_label  
                                text: ""
                                color: "#09FF43"
                                bold: True
                                font_size: "18dp"
                                halign: "center"
                                pos_hint: {'center_y': .72}
                                
                            MDTextField:
                                id: UsernameLogin
                                hint_text: "Username"
                                icon_right: "account"
                                helper_text: "Enter username"
                                helper_text_mode: "on_focus"
                                font_size: "20dp"
                                size_hint_x: .85
                                pos_hint: {'center_x': .5, 'center_y': .65}
                                on_text: self.text = self.text.replace(" ", "")
                                write_tab: False

                            MDTextField:
                                id: PasswordLogin
                                hint_text: "Password"
                                password: True
                                icon_right: "eye-off"
                                helper_text: "Enter password"
                                helper_text_mode: "on_focus"
                                font_size: "20dp"
                                size_hint_x: .85
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                on_text: self.text = self.text.replace(" ", "")
                                write_tab: False
                            BoxLayout: 
                                size_hint: .85, None
                                height: "30dp"
                                pos_hint: {'center_x': .5, 'center_y': .4}
                                spacing: '5dp'

                                MDCheckbox:
                                    id: cb
                                    size_hint: None, None
                                    width: "30dp"
                                    height: "30dp"
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_press: 
                                        PasswordLogin.password = False  if PasswordLogin.password == True else True
                                        PasswordLogin.icon_right = "eye" if PasswordLogin.icon_right == "eye-off" else "eye-off"

                                MDLabel:
                                    text: "[ref=Show Password]Show Password[/ref]"
                                    markup: True
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_ref_press:
                                        cb.active = False if cb.active == True else True
                                        PasswordLogin.password = False  if PasswordLogin.password == True else True
                                    


                            BoxLayout: 
                                size_hint: .6, None
                                height: "30dp"
                                pos_hint: {'center_x': .5, 'center_y': .3}
                                spacing: '15dp'


                                MDRectangleFlatIconButton:
                                    text: "Log In"
                                    icon: "account-check"
                                    font_size: "22dp"
                                    size_hint_x: 1
                                    md_bg_color: "FF5623"
                                    on_release: app.validate_login()

                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Signup'
                            icon: 'account-plus'

                            Image:
                                source: "img/sunset.jpg "
                                size_hint: None, None
                                width: "960dp"
                                height: "1440dp"
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                opacity: 0.5
                            Image:
                                source: "img/Ubraen.png "
                                size_hint: None, None
                                width: "80dp"
                                height: "80dp"
                                pos_hint: {'center_x': .5, 'center_y': .9}
                        
                            MDLabel:
                                text: "Ubraek"
                                color: "#F8F7F7"
                                bold: True
                                font_size: "48dp"
                                halign: "center"
                                pos_hint: {'center_y': .79}
                            MDLabel:
                                id: error_label
                                text: ""
                                color: "#09FF43"
                                bold: True
                                font_size: "18dp"
                                halign: "center"
                                pos_hint: {'center_y': .72}
                                
                            MDTextField:
                                id: Username
                                hint_text: "Username"
                                icon_right: "account"
                                helper_text: "Enter username"
                                helper_text_mode: "on_focus"
                                font_size: "20dp"
                                size_hint_x: .85
                                pos_hint: {'center_x': .5, 'center_y': .65}

                            MDTextField:
                                id: Password
                                hint_text: "Password"
                                password: True
                                icon_right: "eye-off"
                                helper_text: "Enter password"
                                helper_text_mode: "on_focus"
                                font_size: "20dp"
                                size_hint_x: .85
                                pos_hint: {'center_x': .5, 'center_y': .5}
                            

                            BoxLayout: 
                                size_hint: .85, None
                                height: "30dp"
                                pos_hint: {'center_x': .5, 'center_y': .4}
                                spacing: '5dp'

                                MDCheckbox:
                                    id: cb
                                    size_hint: None, None
                                    width: "30dp"
                                    height: "30dp"
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_press: 
                                        Password.password = False  if Password.password == True else True
                                        Password.icon_right = "eye" if Password.icon_right == "eye-off" else "eye-off"

                                MDLabel:
                                    text: "[ref=Show Password]Show Password[/ref]"
                                    markup: True
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_ref_press:
                                        cb.active = False if cb.active == True else True
                                        Password.password = False  if Password.password == True else True
                            BoxLayout: 
                                size_hint: .6, None
                                height: "30dp"
                                pos_hint: {'center_x': .5, 'center_y': .3}
                                spacing: '15dp'

                                MDRectangleFlatIconButton:
                                    text: "Sign Up"
                                    icon: "account-plus"
                                    font_size: "22dp"
                                    size_hint_x: 1
                                    md_bg_color: "FF5623"
                                    on_release: app.validate_signup()