"use strict";

const state = {
  language: localStorage.getItem("bprei-language") || "de",
  countersStarted: false
};

const translatable = document.querySelectorAll("[data-de][data-en]");
const languageButtons = document.querySelectorAll("[data-language]");
const navbar = document.querySelector(".glass-nav");
const navLinks = document.querySelectorAll(".nav-link");
const backTop = document.getElementById("backTop");
const previewShell = document.getElementById("previewShell");

function setLanguage(language) {
  state.language = language === "en" ? "en" : "de";
  localStorage.setItem("bprei-language", state.language);
  document.documentElement.lang = state.language;

  translatable.forEach((element) => {
    element.textContent = element.dataset[state.language];
  });

  languageButtons.forEach((button) => {
    const active = button.dataset.language === state.language;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", String(active));
  });

  const backLabel = state.language === "de" ? "Nach oben" : "Back to top";
  backTop.setAttribute("aria-label", backLabel);
}

function initializeReveal() {
  const elements = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    elements.forEach((element) => element.classList.add("visible"));
    return;
  }

  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        currentObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

  elements.forEach((element) => observer.observe(element));
}

function animateCounters() {
  if (state.countersStarted) return;
  state.countersStarted = true;

  document.querySelectorAll("[data-counter]").forEach((element) => {
    const target = Number(element.dataset.counter);
    const suffix = element.dataset.suffix || "";
    const start = performance.now();
    const duration = 1100;

    function frame(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      element.textContent = `${Math.round(target * eased)}${suffix}`;
      if (progress < 1) requestAnimationFrame(frame);
    }

    requestAnimationFrame(frame);
  });
}

function initializeCounters() {
  const stats = document.querySelector(".stats-band");
  if (!stats || !("IntersectionObserver" in window)) {
    animateCounters();
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    if (entries.some((entry) => entry.isIntersecting)) {
      animateCounters();
      observer.disconnect();
    }
  }, { threshold: 0.25 });

  observer.observe(stats);
}

function updateNavigation() {
  const offset = window.scrollY + 140;
  let activeId = "home";
  document.querySelectorAll("main section[id]").forEach((section) => {
    if (section.offsetTop <= offset) activeId = section.id;
  });

  navLinks.forEach((link) => {
    link.classList.toggle("active", link.getAttribute("href") === `#${activeId}`);
  });
}

function handleScroll() {
  navbar?.classList.toggle("scrolled", window.scrollY > 20);
  backTop?.classList.toggle("visible", window.scrollY > 650);
  updateNavigation();
}

function initializeParallax() {
  if (!previewShell || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const preview = previewShell.querySelector(".preview-window");

  previewShell.addEventListener("mousemove", (event) => {
    const rect = previewShell.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width - 0.5;
    const y = (event.clientY - rect.top) / rect.height - 0.5;
    preview.style.transform = `rotateY(${x * 7 - 4}deg) rotateX(${-y * 6 + 2}deg) translateY(-2px)`;
  });

  previewShell.addEventListener("mouseleave", () => {
    preview.style.transform = "";
  });
}

languageButtons.forEach((button) => {
  button.addEventListener("click", () => setLanguage(button.dataset.language));
});

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    const navigation = document.getElementById("navigation");
    if (navigation?.classList.contains("show")) {
      bootstrap.Collapse.getOrCreateInstance(navigation).hide();
    }
  });
});

backTop?.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
window.addEventListener("scroll", handleScroll, { passive: true });

document.getElementById("year").textContent = String(new Date().getFullYear());
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((element) => new bootstrap.Tooltip(element));

setLanguage(state.language);
initializeReveal();
initializeCounters();
initializeParallax();
handleScroll();
