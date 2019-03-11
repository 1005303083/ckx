$(function () {
    var index = $.cookie('index')
    console.log(index)
    if (index){ // 有点击，有下标
        $('.type-slider li').eq(index).addClass('active')
    } else {
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        $.cookie('index', $(this).index(), {expires: 3, path: '/'})
    })
    
    
    // 子类
    var categoryShow = false
    $('#category-bt').click(function () {
        categoryShow = !categoryShow
        categoryShow ? categoryViewShow() : categoryViewHide()

        console.log('子类点击')
    })

    function categoryViewShow() {
        $('.category-view').show()
        $('#category-bt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')

        sortViewHide()
        sortShow = false
    }

    function categoryViewHide() {
        $('.category-view').hide()
        $('#category-bt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    }
    
    // 排序
    var sortShow = false
    $('#sort-bt').click(function () {
        sortShow = !sortShow
        sortShow ? sortViewShow() : sortViewHide()

        console.log('排序点击')
    })

    function sortViewShow() {
        $('.sort-view').show()
        $('#sort-bt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')

        categoryViewHide()
        categoryShow = false
    }

    function sortViewHide() {
        $('.sort-view').hide()
        $('#sort-bt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    }

    $('.bounce-view').click(function () {
        sortViewHide()
        sortShow = false

        categoryViewHide()
        categoryShow = false
    })
})