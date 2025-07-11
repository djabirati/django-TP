console.log("Script feedback.js chargé");

document.addEventListener("DOMContentLoaded", function () {
    const jobId = window.jobId;
    if (!jobId) {
        console.error("jobId non trouvé !");
        return;
    }

    fetch(`/api/feedback/?job=${jobId}`)
        .then(res => res.json())
        .then(data => {
            console.log("Feedbacks reçus :", data);
            const list = document.getElementById("feedback-list");
            list.innerHTML = "";

            if (data.length === 0) {
                list.innerHTML = `<p>Aucun feedback trouvé.</p>`;
                return;
            }

            data.forEach(feedback => {
                const name = feedback.candidate?.name || "Anonyme";
                const comment = feedback.comment || "";
                const rating = feedback.rating || 0;
                const createdAt = feedback.created_at
                    ? new Date(feedback.created_at).toLocaleDateString("fr-FR")
                    : "";

                const div = document.createElement("div");
                div.className = "bg-white p-4 rounded-xl shadow-sm border";
                div.innerHTML = `
                    <div class="flex justify-between items-center">
                        <p class="text-lg font-semibold">${name}</p>
                        <span class="text-sm bg-gray-200 px-3 py-1 rounded-full">
                            ${rating} ⭐
                        </span>
                    </div>
                    <p class="mt-2 text-gray-700">${comment}</p>
                    <p class="mt-1 text-sm text-gray-500">Posté le ${createdAt}</p>
                `;
                list.appendChild(div);
            });
        })
        .catch(error => {
            console.error("Erreur lors de la récupération des feedbacks:", error);
            const list = document.getElementById("feedback-list");
            list.innerHTML = `<p class="text-red-500">Erreur lors du chargement des feedbacks.</p>`;
        });

    const form = document.getElementById("feedback-form");
    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            const formData = new FormData(form);

            fetch("/api/feedback/", {
                method: "POST",
                body: formData,
                header: {
                    "Authorization": "Token fa708457ca095ec7c66ba01d2d759e1eca1c1121"
                }
            })
                .then(res => {
                    if (!res.ok) throw new Error("Erreur lors de l'envoi du feedback");
                    return res.json();
                })
                .then(() => {
                    form.reset(); // Vide les champs

                    fetch(`/api/feedback/?job=${jobId}`)
                        .then(res => res.json())
                        .then(data => {
                            const list = document.getElementById("feedback-list");
                            list.innerHTML = "";

                            if (data.length === 0) {
                                list.innerHTML = `<p>Aucun feedback trouvé.</p>`;
                                return;
                            }

                            data.forEach(feedback => {
                                const name = feedback.candidate?.name || "Anonyme";
                                const comment = feedback.comment || "";
                                const rating = feedback.rating || 0;
                                const createdAt = feedback.created_at
                                    ? new Date(feedback.created_at).toLocaleDateString("fr-FR")
                                    : "";

                                const div = document.createElement("div");
                                div.className = "bg-white p-4 rounded-xl shadow-sm border";
                                div.innerHTML = `
                                    <div class="flex justify-between items-center">
                                        <p class="text-lg font-semibold">${name}</p>
                                        <span class="text-sm bg-gray-200 px-3 py-1 rounded-full">
                                            ${rating} ⭐
                                        </span>
                                    </div>
                                    <p class="mt-2 text-gray-700">${comment}</p>
                                    <p class="mt-1 text-sm text-gray-500">Posté le ${createdAt}</p>
                                `;
                                list.appendChild(div);
                            });
                        });
                })
                .catch(error => {
                    console.error("Erreur lors de l'envoi du feedback :", error);
                    alert("Erreur lors de l'envoi du feedback.");
                });
        });
    }

});
