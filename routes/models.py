from django.db import models

class AirportRoute(models.Model):
    POSITION_CHOICES = [
        ('L', 'Left'),
        ('R', 'Right'),
    ]

    airport_code = models.CharField(max_length=10, unique=True)

    distance = models.PositiveIntegerField(
        help_text="Duration or distance value"
    )

    connected_airport = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    position = models.CharField(
        max_length=1,
        choices=POSITION_CHOICES,
        default='L',
        help_text="Position relative to connected airport"
    )

    def __str__(self):
        return self.airport_code