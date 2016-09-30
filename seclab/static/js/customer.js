$(document).ready(function()
{
	$('.fmenu').hover(
		function()
		{
			$(this).addClass('active')
		},
		function()
		{
			$(this).removeClass('active')
		})

	$('.has_son_True').addClass('dropdown')
	$('.has_son_True').children('a').addClass('dropdown-toggle')
	$('.has_son_True').children('a').attr("data-toggle","dropdown")
	$('.has_son_True').children('a').append('<b class="caret"></b>')

	$('.has_son_True').hover(
		function()
		{
			$(this).addClass('open')
		},
		function()
		{
			$(this).removeClass('open')
		})

	$('.my-panel-header').hover(
		function()
		{
			$(this).animate({left:'8px',fontSize:'21px'},'fast');
			console.log("1")
		},
		function()
		{
			$(this).animate({left:'0px',fontSize:'20px'},'fast');
			console.log("2")
		})

	$('#homeSlider').hover(
		function()
		{
			$('.carousel-control').fadeIn('fast')
		},
		function()
		{
			$('.carousel-control').fadeOut('fast')
		})

	$('.img_0').addClass('active')	//首页轮播，默认是最先使第一张图片(id=0)active
})