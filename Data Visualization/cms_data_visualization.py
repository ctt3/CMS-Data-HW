# Import dependencies
import numpy as np
import pandas as pd
from bokeh.models import HoverTool
from bokeh.charts import Donut, show, output_file
from bokeh.io import output_notebook


# Read Data
medicaid_summary = pd.read_csv('./MSIS2012 Table17.csv', index_col="STATE")

#Transpose, exclude total and empty row
medicaid_summary = medicaid_summary.T[1:-1]

#Initialize HoverTool for tooltip category display
hover = HoverTool(
        tooltips=
        """
            <div>
                <span style="font-size: 10px; font-weight: bold;">@index</span>
            </div>
        """
    )

#Initialize Donut object display
chart = Donut(medicaid_summary,
            title="Medicaid Payments by Service Category",
            values='TOTAL',
            text_font_size='0pt',
            tools=[hover]
           )

# Output to static HTML file
output_file("medicaid_summary.html", title="Medicaid Payments by Service Category")

# Open HTML file and display Donut Visualization
show(chart)