// custom editor
var VehicleSelectorWidget = function(args) {

    // 1. Find a current color setting in the annotation, if any
    var currentColorBody = args.annotation ? 
    args.annotation.bodies.find(function(b) {
        return b.purpose == 'highlighting';
    }) : null;

    // 2. Keep the value in a variable
    var currentColorValue = currentColorBody ? currentColorBody.value : null;

    // 3. Triggers callbacks on user action
    var addTag = function(evt) {
        if (currentColorBody) {
            args.onUpdateBody(currentColorBody, {
            type: 'TextualBody',
            purpose: 'highlighting',
            value: evt.target.dataset.tag
            });
        } else { 
            args.onAppendBody({
            type: 'TextualBody',
            purpose: 'highlighting',
            value: evt.target.dataset.tag
            });
        }
    }

    // 4. This part renders the UI elements
    var createButton = function(value) {
        console.log('createbutton function')
        var button = document.createElement('button');
        console.log(currentColorValue)

        if (value == currentColorValue)
            button.className = 'selected';

        button.dataset.tag = value;
        button.style.backgroundColor = value;
        button.addEventListener('click', addTag); 
        return button;
    }

    var container = document.createElement('div');
    container.className = 'colorselector-widget';

    var button1 = createButton('RED');
    var button2 = createButton('GREEN');
    var button3 = createButton('BLUE');

    container.appendChild(button1);
    container.appendChild(button2);
    container.appendChild(button3);

    return container;
}

var VehicleFormatter = function(annotation) {
    var highlightBody = annotation.bodies.find(function(b) {
        return b.purpose == 'highlighting';
    });

    if (highlightBody)
        return highlightBody.value;
}