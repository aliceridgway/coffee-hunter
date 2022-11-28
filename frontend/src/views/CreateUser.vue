<script setup>
import { ref } from "vue";

const username = ref(null);
const usernameRules = ref({
  required: (value) => !!value || "Required.",
  min: (v) => v.length < 6 || "Min 6 characters",
});

const password = ref(null);
const confirmPassword = ref(null);
const passwordRules = ref({
  required: (value) => !!value || "Required.",
  min: (v) => v.length >= 8 || "Min 8 characters",
});
</script>

<template>
  <v-form ref="form">
    <v-text-field
      v-model="username"
      label="Username"
      :rules="[usernameRules.required, usernameRules.min]"
    ></v-text-field>
    <v-text-field
      v-model="password"
      label="Password"
      :type="'password'"
      :rules="[passwordRules.required, passwordRules.min]"
    ></v-text-field>
    <v-text-field
      v-model="confirmPassword"
      label="Confirm Password"
      :type="'password'"
      :rules="[passwordRules.required, passwordRules.min]"
    ></v-text-field>

    <v-btn type="submit">Register</v-btn>
  </v-form>
</template>