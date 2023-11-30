You can add files into this folder and they will be available to your extension by calling self.get_template.

For instance:

async def q2_post(self):
    ...
    html_template = self.get_template('foo.html', {'this': 'that'})
    return html_template

This line would load the template stored in templates/foo.html, substituting
{{this}} with 'that'. This uses the popular jinja templating library. For
more info, refer to http://jinja.pocoo.org/

You can also use custom jinja filters by defining them in templates/filters.py. The registered filter
will use the same name as your defined method. For more information about creating custom jinja
filters, refer to http://jinja.pocoo.org/docs/2.10/api/#writing-filters.
