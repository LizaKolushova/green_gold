<template>
    <input
        type="checkbox"
        :name="name"
        :id="name"
        :value="value"
        @input="$emit('input', $event.target.value)"
        class="form__checkbox"
    >
</template>

<script>
export default {
    name: "FormCheckbox",
    emits: ['update:modelValue'],
    props: {
        name: {
            type: String,
            required: true
        },
        value: {
            type: [Boolean, String],
            required: true
        }
    }
}
</script>
