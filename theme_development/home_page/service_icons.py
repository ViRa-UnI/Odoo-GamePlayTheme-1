```python
import svglib
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def renderServiceIcons():
    # Define the SVG icons
    icons = ["icon1.svg", "icon2.svg", "icon3.svg", "icon4.svg"]

    # Create a four-column grid for the icons
    html = '<div class="service-icons-grid">'

    for icon in icons:
        # Convert SVG to PNG for better browser compatibility
        drawing = svg2rlg(icon)
        renderPM.drawToFile(drawing, icon.replace('.svg', '.png'), fmt="PNG")

        # Add the icon to the grid with hover animation
        html += f'''
        <div class="service-icon">
            <img src="{icon.replace('.svg', '.png')}" alt="Service Icon" onmouseover="this.style.transform='scale(1.2)';" onmouseout="this.style.transform='scale(1)';">
        </div>
        '''

    html += '</div>'

    # Insert the grid into the service icons section
    document.getElementById('serviceIcons').innerHTML = html
```