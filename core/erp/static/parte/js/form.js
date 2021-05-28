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

$('#tblOrdenes').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        },
        dataSrc: ""
    },
    columns: [
        { "data": "impresora_id" },
        { "data": "nombre" },
        { "data": "option" },
        {"data": "created"},
        {"data": "modified"},
        {"data": "activo"},
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
        console.log('cargado');
    }
});
$('#tblParteCabecera').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    "searching": false,
    "bPaginate": false,
    "ordering": false,
    "info": false,
    ajax: {
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        },
        dataSrc: ""
    },
    columns: [
        // { "data": "impresoras.activo" },
        // { "data": "categoria.id" },
        // { "data": "ayudante1ero" },
        // { "data": "ayudante2do" },
        // { "data": "impresora.nombre" },
        // { "data": "pedido_venta.fichaTecnica" },
        // { "data": "options" },
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
        {
            targets: [0],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '<select name="" class="form-control"><option>Coche</option><option>Avión</option><option>Tren</option></select>'
            }
        },
    ],
    initComplete: function (settings, json) {

    }
});
$('#tblParteCuerpo').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    "searching": false,
    "bPaginate": false,
    "ordering": false,
    "info": false,
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
tblCambio = $('#tblCambios').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    "searching": false,
    "ordering": false,
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
        { "data": "create" },
        { "data": "parada.id" },
        { "data": "fecha_fin" },
    ],
    columnDefs: [
        {
            targets: [0],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var buttons = '<a href="/erp/parada/tomado/' + row.id + '/" class="btn btn-warning btn-flat border-dark rounded-lg"><i class="fas fa-edit"></i></a> ';
                buttons += '<a href="/erp/parada/delete/' + row.id + '/" type="button" class="btn btn-danger btn-flat border-dark rounded-lg"><i class="fas fa-trash-alt"></i></a>';
                return buttons;
            }
        },
        {
            targets: [4],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var buttons = '<a href="/erp/parada/tomado/' + row.id + '/" class="btn btn-success btn-lg btn-flat border border-dark rounded-circle"><i class="fas fa-file-download"></i></a> ';
                return buttons;
            }
        },
    ],
    initComplete: function (settings, json) {

    }
});