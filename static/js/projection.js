var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
         console.log('connected');
    });
    socket.on('message', function(data) {
         // console.log(data);
    });
