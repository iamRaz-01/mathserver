from django.shortcuts import render
    
def calculate_values(request):
    context = {
        'power': '',
        'intensity': '',
        'resistance': ''
    }

    if request.method == 'POST':
        print("POST method is used")

        # Get input values from the form
        resistance = request.POST.get('resistance', '0')
        intensity = request.POST.get('intensity', '0')

        print('Request:', request)

        try:
            # Convert inputs to float for calculations
            resistance = float(resistance)
            intensity = float(intensity)

            power = intensity**2*resistance

            # Update the context with calculated values
            context['resistance'] = round(resistance, 2)
            context['power'] = round(power, 2)
            context['intensity'] = round(intensity, 2)

            print('Power:', power)
            print('Intensity:', intensity)
            print('Resistance:', resistance)

        except ValueError:
            # Handle invalid input values
            context['error'] = "Invalid input. Please enter numeric values."

    return render(request, 'serverApp/mathServer.html', context)
