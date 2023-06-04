{% extends 'core/base.html' %}

{% block head_title %}Bank online{% endblock %}

{% block content %}
{% if registration_form.non_field_errors %}
    {% for error in registration_form.non_field_errors %}
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mt-2" role="alert">
        <p class="font-bold">Error!</p>
        <p class="block sm:inline">{{ error }}</p>
    </div>
    {% endfor %}
{% endif %}
{% if address_form.non_field_errors %}
    {% for error in address_form.non_field_errors %}
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mt-2" role="alert">
        <p class="font-bold">Error!</p>
        <p class="block sm:inline">{{ error }}</p>
    </div>
    {% endfor %}
{% endif %}

<h1 class="font-mono font-bold text-3xl text-center pb-5 pt-10">Register</h1>
<hr />
<div class="w-full mt-10">
    <form method="post" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        {% csrf_token %}
        {% for hidden_field in registration_form.hidden_fields %}
            {{ hidden_field.errors }}
            {{ hidden_field }}
        {% endfor %}
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.first_name.id_for_label }}">
                    {{ registration_form.first_name.label }}
                </label>
                {{ registration_form.first_name }}
                {% if registration_form.first_name.errors %}
                    {% for error in registration_form.first_name.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
            <div class="w-full md:w-1/2 px-3">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.last_name.id_for_label }}">
                    {{ registration_form.last_name.label }}
                </label>
                {{ registration_form.last_name }}
                {% if registration_form.last_name.errors %}
                    {% for error in registration_form.last_name.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.email.id_for_label }}">
                    {{ registration_form.email.label }}
                </label>
                {{ registration_form.email }}
                {% if registration_form.email.errors %}
                    {% for error in registration_form.email.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.account_type.id_for_label }}">
                    {{ registration_form.account_type.label }}
                </label>
                {{ registration_form.account_type }}
                {% if registration_form.account_type.errors %}
                    {% for error in registration_form.account_type.errors %}
                    <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.gender.id_for_label }}">
                    {{ registration_form.gender.label }}
                </label>
                {{ registration_form.gender }}
                {% if registration_form.gender.errors %}
                    {% for error in registration_form.gender.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.birth_date.id_for_label }}">
                    {{ registration_form.birth_date.label }}
                </label>
                {{ registration_form.birth_date }}
                {% if registration_form.birth_date.errors %}
                    {% for error in registration_form.birth_date.errors %}
                    <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.password1.id_for_label }}">
                    {{ registration_form.password1.label }}
                </label>
                {{ registration_form.password1 }}
                {% if registration_form.password1.errors %}
                    {% for error in registration_form.password1.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ registration_form.password2.id_for_label }}">
                    {{ registration_form.password2.label }}
                </label>
                {{ registration_form.password2 }}
                    {% if registration_form.password2.errors %}
                    {% for error in registration_form.password2.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
        </div>

        {% for hidden_field in address_form.hidden_fields %} {{ hidden_field.errors }} {{ hidden_field }} {% endfor %}
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ address_form.street_address.id_for_label }}">
                    {{ address_form.street_address.label }}
                </label>
                {{ address_form.street_address }}
                {% if address_form.street_address.errors %}
                    {% for error in address_form.street_address.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
            <div class="w-full md:w-1/2 px-3">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ address_form.city.id_for_label }}">
                    {{ address_form.city.label }}
                </label>
                {{ address_form.city }}
                {% if address_form.city.errors %}
                    {% for error in address_form.city.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ address_form.postal_code.id_for_label }}">
                    {{ address_form.postal_code.label }}
                </label>
                {{ address_form.postal_code }}
                {% if address_form.postal_code.errors %}
                    {% for error in address_form.postal_code.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
            <div class="w-full md:w-1/2 px-3">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="{{ address_form.country.id_for_label }}">
                    {{ address_form.country.label }}
                </label>
                {{ address_form.country }}
                {% if address_form.country.errors %}
                    {% for error in address_form.country.errors %}
                        <p class="text-red-600 text-sm italic pb-2">{{ error }}</p>
                    {% endfor %}
                {% endif %}
            </div>
        </div>
        <div class="flex items-center justify-between">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                Register
            </button>
        </div>
    </form>
</div>
{% endblock %}
