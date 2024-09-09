from rest_framework import serializers

class CalculatorInputSerializer(serializers.Serializer):
    month1 = serializers.FloatField()
    month2 = serializers.FloatField()
    month3 = serializers.FloatField()
    distributor_tax = serializers.FloatField()
    tax_type = serializers.ChoiceField(choices=[('Residencial', 'Residencial'), ('Comercial', 'Comercial'), ('Industrial', 'Industrial')])

class CalculatorOutputSerializer(serializers.Serializer):
    annual_savings = serializers.FloatField()
    monthly_savings = serializers.FloatField()
    applied_discount = serializers.FloatField()
    coverage = serializers.FloatField()