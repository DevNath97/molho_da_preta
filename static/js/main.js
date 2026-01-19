// ==================================================
// Arquivo JS global do site
// Responsável por interações básicas (menu mobile)
// ==================================================

document.addEventListener("DOMContentLoaded", function () {

    /* ==============================================
       MENU MOBILE (TOGGLE)
       ============================================== */

    const menuToggle = document.querySelector(".menu-toggle");
    const menuLista = document.querySelector(".menu ul");

    // Segurança: só executa se os elementos existirem
    if (menuToggle && menuLista) {

        // Estado inicial de acessibilidade
        menuToggle.setAttribute("aria-expanded", "false");

        menuToggle.addEventListener("click", function () {

            // Alterna menu
            const menuAberto = menuLista.classList.toggle("active");

            // Atualiza acessibilidade
            menuToggle.setAttribute(
                "aria-expanded",
                menuAberto ? "true" : "false"
            );
        });
    }

    /* ==============================================
       FECHAR MENU AO CLICAR EM UM LINK (MOBILE)
       ============================================== */

    const menuLinks = document.querySelectorAll(".menu ul a");

    menuLinks.forEach(function (link) {
        link.addEventListener("click", function () {

            if (menuLista && menuLista.classList.contains("active")) {
                menuLista.classList.remove("active");

                if (menuToggle) {
                    menuToggle.setAttribute("aria-expanded", "false");
                }
            }
        });
    });

});
