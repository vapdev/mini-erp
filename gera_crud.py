import sys
import os

# Function to generate Vue 3 CRUD component code
def generate_vue_crud_component(title, is_irregular_plural):
    # Determine the plural form based on the is_irregular_plural flag
    plural_suffix = "es" if is_irregular_plural else "s"

    vue_code = f'''
<script setup>
  const columns = ref([
    {{
      name: 'id',
      required: true,
      label: 'ID',
      align: 'left',
      field: 'id',
      sortable: true
    }},
    {{
      name: 'criado_em',
      align: 'left',
      label: 'Criado em',
      field: 'created_at',
      sortable: true
    }},
  ]);

  const form = ref({{
    checkboxField: false, // Initialize checkbox field
    inputField: '',       // Initialize input field
    selectField: '',      // Initialize select field
    toggleField: false,   // Initialize toggle field
  }});
</script>

<template>
  <q-page padding>
    <PageTitle title="{title}" />
    <SimpleCrud title="{title}" v-model="form" :columns="columns" api_route="{title.lower()}{plural_suffix}">
      <!------ SLOT DO CONTEUDO DO DIALOG ------>

      <!-- Checkbox -->
      <q-checkbox v-model="form.checkboxField" label="Checkbox Label" />
      <!-- Input -->
      <q-input v-model="form.inputField" label="Input Label" />
      <!-- Select -->
      <q-select v-model="form.selectField" label="Select Label" :options="['Option 1', 'Option 2', 'Option 3']" />
      <!-- Toggle -->
      <q-toggle v-model="form.toggleField" label="Toggle Label" />

      <!------ SLOT DO CONTEUDO DO DIALOG ------>
    </SimpleCrud>
  </q-page>
</template>
'''
    return vue_code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <custom_title> [is_irregular_plural]")
        sys.exit(1)

    custom_title = sys.argv[1]
    is_irregular_plural = sys.argv[2].lower() == "true" if len(sys.argv) > 2 else False  # Set default to False

    generated_code = generate_vue_crud_component(custom_title, is_irregular_plural)

    # Determine the filename based on the plural form
    plural_suffix = "es" if is_irregular_plural else "s"

    # Save the generated code to a .vue file in the 'pages' folder
    pages_folder = "pages"
    file_path = os.path.join(pages_folder, f"{custom_title.lower()}{plural_suffix}.vue")

    # Ensure the 'pages' folder exists, create it if not
    os.makedirs(pages_folder, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(generated_code)

    print(f"Vue 3 CRUD component with title '{custom_title}' and {'irregular' if is_irregular_plural else 'regular'} plural generated successfully in the 'pages' folder.")
