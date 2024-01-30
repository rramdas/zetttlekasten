from django.db import models

class Note(models.Model):
    """
    Represents an individual note in the Zettelkasten system.

    Attributes:
        title (models.CharField): The title of the note.
        content (models.TextField): The content of the note.
        created_at (models.DateTimeField): The date and time when the note was created.
        updated_at (models.DateTimeField): The date and time when the note was last updated.
        tags (models.ManyToManyField): The tags associated with the note.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        """Returns a string representation of the note, primarily for admin or debug purposes."""
        return self.title

class Tag(models.Model):
    """
    Represents a tag that can be associated with notes.

    Attributes:
        name (models.CharField): The name of the tag.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Returns the tag's name."""
        return self.name

class Link(models.Model):
    """
    Represents a directional link from one note to another within the Zettelkasten system.

    Attributes:
        from_note (models.ForeignKey): The note where the link originates.
        to_note (models.ForeignKey): The note where the link points to.
    """
    from_note = models.ForeignKey(Note, related_name='outgoing_links', on_delete=models.CASCADE)
    to_note = models.ForeignKey(Note, related_name='incoming_links', on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of the link between two notes."""
        return f"{self.from_note.title} -> {self.to_note.title}"
