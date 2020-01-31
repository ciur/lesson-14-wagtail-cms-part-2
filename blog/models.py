from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class Lesson(Page):
    body = RichTextField()

    content = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('premium_paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('premium_embed', EmbedBlock()),
        ('embed', EmbedBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        StreamFieldPanel('content'),
    ]
