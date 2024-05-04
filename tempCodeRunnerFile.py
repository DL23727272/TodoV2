      # Check if the current content is already displayed
        current_widget = self.root.ids.container.children
        if current_widget and isinstance(current_widget[0], ListItemWithCheckbox):
            # If the current content is already displayed, return without reloading
            return

        # If the current content is different or not yet loaded, reload it
        self.root.ids.container.clear_widgets()
        self.on_start()