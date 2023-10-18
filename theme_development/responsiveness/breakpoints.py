```python
# Import necessary libraries
from responsive_breakpoints import ResponsiveBreakpoints

# Define breakpoints for different screen sizes
breakpoints = ResponsiveBreakpoints()

# Mobile breakpoint
breakpoints.mobile = 480

# Tablet breakpoint
breakpoints.tablet = 768

# Desktop breakpoint
breakpoints.desktop = 1024

# Function to get current breakpoint
def get_current_breakpoint(width):
    if width <= breakpoints.mobile:
        return 'mobile'
    elif width <= breakpoints.tablet:
        return 'tablet'
    else:
        return 'desktop'

# Function to handle breakpoint changes
def handle_breakpoint_change():
    current_breakpoint = get_current_breakpoint(window.innerWidth)
    if current_breakpoint != breakpoints.current:
        breakpoints.current = current_breakpoint
        window.dispatchEvent(new CustomEvent('breakpointChange', { 'detail': current_breakpoint }))

# Listen for window resize event
window.addEventListener('resize', handle_breakpoint_change)

# Initialize current breakpoint
handle_breakpoint_change()
```