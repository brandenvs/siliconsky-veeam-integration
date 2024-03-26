jQuery(document).ready(function ($) {
  // Terms & Discounts
  var termArr = [1, 12, 24, 36],
    discArr = [0, 0.2, 0.25, 0.3];

  // Custom Region Pricing
  var prices = {
    ca: [0.12, 0.11, 0.1],
    az: [0.12, 0.11, 0.1],
    va: [0.12, 0.11, 0.1],
    sg: [0.2, 0.19, 0.18],
    th: [0.2, 0.19, 0.18],
    hk: [0.2, 0.19, 0.18],
  };

  // Exchange Rates & Symbols
  var exchange = {
    rates: {
      USD: 1,
      CNY: 6.92,
      THB: 35,
    },
    symbol: {
      USD: "$",
      CNY: "¥",
      THB: "฿",
    },
  };

  // Total TB Slider
  $("#gb-slider")
    .slider({
      range: "min",
      value: 2000,
      step: 500,
      max: 10000,
      min: 1000,
      slide: function (event, ui) {
        if (ui.value < 10000) {
          $(".contact-us").fadeOut(200, function () {
            $(".price-wrap").fadeIn(200);
          });
          var term = $("#term-slider").slider("option", "value");
          $('[name="qty"]').val(ui.value);
          $("#total-price .price").text(calcPrice(ui.value, term));
          $("#price-per-gb .price").html(pricePerGB(ui.value).toFixed(2));
          $('[name="unit_price"]').val(pricePerGB(ui.value).toFixed(2));
        } else {
          $(".price-wrap").fadeOut(200, function () {
            $(".contact-us").fadeIn(200);
          });
        }
      },
    })
    .each(function () {
      var opt = $(this).data().uiSlider.options;
      var vals = (opt.max - opt.min) / 1000;
      for (var i = 0; i <= vals; i++) {
        var el = $('<label class="value-label">' + (i + 1) + "TB</label>").css(
          "left",
          "calc(" + (i / vals) * 100 + "% - 10px)"
        );
        $(this).append(el);
      }
    });

  // Contract Slider
  $("#term-slider")
    .slider({
      range: "min",
      max: termArr.length - 1,
      slide: function (event, ui) {
        var size = $("#gb-slider").slider("option", "value");
        $('[name="period"]').val(termArr[ui.value]);
        $("#total-price .price").text(calcPrice(size, ui.value));
        $('[name="discount_term"]').val(discArr[ui.value]);
      },
    })
    .each(function () {
      var opt = $(this).data().uiSlider.options;
      var vals = opt.max - opt.min;
      for (var i = 0; i <= vals; i++) {
        if (i == 0) {
          var el = $('<label class="value-label">Monthly</label>').css(
            "left",
            "0%"
          );
        } else {
          var el = $(
            '<label class="value-label">' + termArr[i] + " Mo.</label>"
          ).css("left", (i / vals) * 95 + "%");
        }
        $(this).append(el);
      }
    });

  // Calcutate Price Per GB
  function pricePerGB(value) {
    var region = $("#region").val();
    if (value <= 2000) {
      return prices[region][0];
    } else if (value <= 4999) {
      return prices[region][1];
    } else if (value <= 10000) {
      return prices[region][2];
    } else {
      return false;
    }
  }

  // Calculate Total Price
  function calcPrice(size, term) {
    var basePrice = size * pricePerGB(size),
      discount = basePrice - basePrice * discArr[term],
      rate = exchange.rates[$("#currency-select").val()],
      price = (discount * rate).toFixed(2);
    return price;
  }

  // Changing Currencies
  $("#currency-select, #region").change(function () {
    var pricePer = pricePerGB(
      $("#gb-slider").slider("option", "value")
    ).toFixed(2);
    $(".currency-symbol").text(exchange.symbol[$(this).val()]);
    $("#total-price .price").text(
      calcPrice(
        $("#gb-slider").slider("option", "value"),
        $("#term-slider").slider("option", "value")
      )
    );
    $('[name="unit_price"]').val(pricePer);
    $("#price-per-gb .price").text(pricePer);
  });

  // Load price when page does
  $("#total-price .price").text(
    calcPrice(
      $("#gb-slider").slider("option", "value"),
      $("#term-slider").slider("option", "value")
    )
  );
  $("#price-per-gb .price").html(
    pricePerGB($("#gb-slider").slider("option", "value")).toFixed(2)
  );
  $('[name="discount_term"]').val(
    discArr[$("#term-slider").slider("option", "value")]
  );

  $("#backup-form").submit(function (e) {
    console.log($(this).serialize());
    e.preventDefault();
  });
});
