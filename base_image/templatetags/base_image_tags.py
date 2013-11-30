from django import template
from base64 import b64encode
from StringIO import StringIO
import Image

register = template.Library()

def base_image(size="1x1"):
    tmp = StringIO()
    str_split = tuple(size.split('x'))
    img = Image.new('RGBA', (int(str_split[0]), int(str_split[1])))
    img.save(tmp, format="PNG")
    encoded = b64encode(tmp.getvalue())
    return 'data:image/png;base64,%s' % encoded

register.simple_tag(base_image)
