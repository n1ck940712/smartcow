// custom editor
var VehicleSelectorWidget = function(args) {

    // 1. Find a current color setting in the annotation, if any
    var currentColorBody = args.annotation ? 
    args.annotation.bodies.find(function(b) {
        return b.purpose == 'vehicle_type';
    }) : null;

    // 2. Keep the value in a variable
    var currentColorValue = currentColorBody ? currentColorBody.value : null;

    // 3. Triggers callbacks on user action
    var addTag = function(evt) {
        console.log($('.vehicleselector-widget').val())
        if (currentColorBody) {
            args.onUpdateBody(currentColorBody, {
            type: 'TextualBody',
            purpose: 'vehicle_type',
            value: evt.target.value
            });
        } else { 
            args.onAppendBody({
            type: 'TextualBody',
            purpose: 'vehicle_type',
            value: evt.target.value
            });
        }
    }

    // 4. This part renders the UI elements
    var createOption = function(value) {
        var option = document.createElement('option');
        console.log(currentColorValue)
        if (value == currentColorValue)
            option.selected = true;

        option.dataset.tag = value;
        option.value = value;
        option.text = value;
        
        
        return option;
    }

    var container = document.createElement('select');
    container.className = 'vehicleselector-widget';
    var label = document.createElement('option');
    label.text = 'Select Type';
    label.disabled = true;
    label.selected = true;
    container.appendChild(label);

    var option1 = createOption('Car');
    var option2 = createOption('Bus');
    var option3 = createOption('Autorickshaw');
    var option4 = createOption('Bike');
    
    container.appendChild(option1);
    container.appendChild(option2);
    container.appendChild(option3);
    container.appendChild(option4);
    // $('.r6o-btn').click(addTag);
    container.addEventListener('change', addTag); 
    
    return container;
}

var VehicleFormatter = function(annotation) {
    console.log('format')
    var vehicle_type = annotation.bodies.find(function(b) {
        return b.purpose == 'vehicle_type';
    });

    if (vehicle_type)
        return vehicle_type.value;
}