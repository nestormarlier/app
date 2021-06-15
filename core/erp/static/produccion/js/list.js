$(function () {
    $('#tblImpresoras').DataTable({
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
            { "data": "impresora_id" },
            { "data": "nombre" },
            { "data": "option" },
            // {"data": "created"},
            // {"data": "modified"},
            // {"data": "activo"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    // paso x el browser el Id seleccionado de la columna impresora_id para que lo tome Parte/create.html
                    var buttons = '<a href="/erp/parte/add/' + row.impresora_id + '" class="btn btn-success btn-lg btn-flat"><i class="fas fa-angle-double-right 2x"></i></a> ';
                    // console.log(row.id);
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            // console.log('cargado');
        }
    });
});