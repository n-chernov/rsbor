ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [59.9241, 30.1],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true
        });

    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set({'preset': 'islands#greenDotIcon', 'hasBalloon':false});
    objectManager.clusters.options.set({'preset': 'islands#greenClusterIcons', 'hasBalloon':false});
    myMap.geoObjects.add(objectManager);

    $.ajax({
        url: "points-for-yandex.json",
		dataType: "json"
    }).done(function(data) {
        objectManager.add(data);
    });

}