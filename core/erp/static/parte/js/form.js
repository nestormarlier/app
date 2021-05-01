var tblOrdenes;
var parte = {
    items: {
        ordenes: [],
        maquinista: '',
        supervisor: '',
        ayudante1ero: '',
        ayudante2do: '',
        create: '',
        cambio: [],
        setup: [],
        produccion: [],
        observacion_gral: [],
        observacion_mant: [],
        metros_registro: 0,
        kg_registro: 0,
        metros: 0,
        kg: 0
    },
    add: function () {

    }
};

$(function () {
    tblOrdenes = $('#tblOrdenes').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "searching": false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "options" },
            { "data": "id" },
            { "data": "impresora.nombre" }, // debe estar en models.py item['impresora']= self.impresora.toJSON()
            { "data": "pedido_venta.id" }, // item['pedido_venta']= self.pedido_venta.toJSON()
            { "data": "pedido_venta.fecha_entrega" }, // item['pedido_venta']= self.pedido_venta.toJSON()
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/parte/tomado/' + row.id + '/" class="btn btn-warning btn-flat border-dark rounded-lg"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/parte/delete/' + row.id + '/" type="button" class="btn btn-danger btn-flat border-dark rounded-lg"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
            {
                targets: [5],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/parte/tomado/' + row.id + '/" class="btn btn-success btn-lg btn-flat border border-dark rounded-circle"><i class="fas fa-file-download"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#tblParteCabecera').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "searching": false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "categoria.id" },
            { "data": "ayudante1ero" },
            { "data": "ayudante2do" },
            // { "data": "impresora.nombre" },
            // // { "data": "pedido_venta.fichaTecnica" },
            // // { "data": "options" },
        ],
        // columnDefs: [
        //     {
        //         targets: [-1],
        //         class: 'text-center',
        //         orderable: false,
        //         render: function (data, type, row) {
        //             var buttons = '<a href="/erp/parte/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
        //             buttons += '<a href="/erp/parte/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
        //             return buttons;
        //         }
        //     },
            // {
            //     targets: [0],
            //     class: 'text-center',
            //     orderable: false,
            //     render: function (data, type, row) {
            //         return '<select name="" class="form-control"><option>Coche</option><option>Avión</option><option>Tren</option></select>'
            //     }
            // },
        // ],
        initComplete: function (settings, json) {
            
        }
    });
    $('#tblParteCuerpo').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "searching": false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "kg_prod" },
            { "data": "kg_producidos" },
            { "data": "mts_prod" },
            { "data": "mts_producidos" },
            { "data": "kg_registro" },
            { "data": "metros_registro" },
            { "data": "options" },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/parte/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/parte/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});