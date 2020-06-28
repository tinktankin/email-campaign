


        //---------------------------------- HEADER AND LEFT PANEL START ---------------------------------------

        var leftpanel = document.querySelector('.leftpanel');
        var pagelinks = leftpanel.getElementsByClassName('pagelink');
        for (var i = 0; i < pagelinks.length; i++) {
            pagelinks[i].addEventListener("click", function() {
                var current = document.getElementsByClassName("active");
                if (current.length > 0){
                    current[0].className = current[0].className.replace(" active", "");
                }
                this.className += " active";
            });
        };

        //---------------------------------- HEADER AND LEFT PANEL END ---------------------------------------

        //----file input replacement to improve UI


        //-----file input replacement end

        //-----add contacts manually window
