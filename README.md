django-base-image
==============

### What does it do
Create base64 encoded transparent pngs for faster page loads.

### Why
Image loading can cause content to shift and bump until all images are loaded.
Instead, create a transparent png with the proper aspect ratio, and load the 
respective image via JavaScript when the page has loaded, or the image is 
near/in view.

### Requires
    PIL

### How can i use it
Install via pip:

    pip install -e git+git://github.com/ericlindstrom/django-base-image.git#egg=django-base-image
    
Add `base_image` to `INSTALLED_APPS` in your settings:

    # settings.py
    INSTALLED_APPS = (
        ...
        'base_image',
    )

In your template, load the template tag

    {% load base_image_tags %}

And use it like 'INTxINT'

    <img src="{% base_image '16x9' %}" />

Which will render a base64 encoded transparent PNG

    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAYAAAA7KqwyAAAAD0lEQVR4nGNgGAWjgAoAAAJJAAHZX3+dAAAAAElFTkSuQmCC" />

## Example
Speed up page by not loading images, until all the rest of your content is loaded, making as few requests as possible.

    <!-- HTML -->

    <img src="{% base_image '16x9' %}" data-src="{{ image.url }}" />
    <noscript>
      <img src="{{ image.url }}" />
    </noscript>

And then in JavaScript, wait for the window to load and replace the `src` with `data-src`.

    // JS / jquery

    $(window).load(function() {
      $('img[data-src]').each(function() {
        $(this).attr('src', $(this).attr('data-src'));
      });
    });

