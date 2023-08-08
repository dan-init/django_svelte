import django_filters
from .models import TestResults, Vehicle, Drivetrace,Cell

class MyRangeWidget(django_filters.widgets.RangeWidget):
    
    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super(MyRangeWidget, self).__init__(attrs)
        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)


class TestResultsFilter(django_filters.FilterSet):
    
    vehicle_id = django_filters.MultipleChoiceFilter(choices = Vehicle.objects.values_list)
    drivetrace = django_filters.MultipleChoiceFilter(choices = Drivetrace.objects.values_list)
    cell = django_filters.MultipleChoiceFilter(choices = Cell.objects.values_list)
    
    iwr = django_filters.RangeFilter(widget=MyRangeWidget(
                                    from_attrs={'placeholder':'min'},
                                    to_attrs={'placeholder':'max'},)
                                    )
    
    total_co2 = django_filters.RangeFilter(
                                     widget=MyRangeWidget(
                                        from_attrs={'placeholder':'min'},
                                        to_attrs={'placeholder':'max'},)
                                    )
    
    total_co = django_filters.RangeFilter(
                                     widget=MyRangeWidget(
                                        from_attrs={'placeholder':'min'},
                                        to_attrs={'placeholder':'max'},)
                                    )
    
    class Meta:

        model = TestResults
        fields = ['vehicle_id', 'drivetrace']
