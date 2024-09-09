from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CalculatorInputSerializer, CalculatorOutputSerializer
from .calculator import calculator  # função calculadora que você já criou
from consumer.models import Consumer

from rest_framework import viewsets


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
  

@api_view(['POST'])
def calculate_savings(request):
    input_serializer = CalculatorInputSerializer(data=request.data)
    if input_serializer.is_valid():
        data = input_serializer.validated_data
        consumption = [data['month1'], data['month2'], data['month3']]
        distributor_tax = data['distributor_tax']
        tax_type = data['tax_type']

        annual_savings, monthly_savings, applied_discount, coverage = calculator(consumption, distributor_tax, tax_type)

        output_data = {
            'annual_savings': annual_savings,
            'monthly_savings': monthly_savings,
            'applied_discount': applied_discount,
            'coverage': coverage,
        }
        output_serializer = CalculatorOutputSerializer(output_data)
        return Response(output_serializer.data)
    return Response(input_serializer.errors, status=400)