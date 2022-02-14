<template>
  <v-card class="mx-auto" max-width="400">
    <v-card-first>{{first_name}}</v-card-first>
    <v-card-last>{{last_name}}</v-card-last>
    <v-card-title>{{title}}</v-card-title>
    <v-card-birth>{{birth_date}}</v-card-birth>
    <v-card-actions>
      <v-spacer></v-spacer>
      <slot name="button"></slot>
     </v-card-actions>
  </v-card>
</template>

<script>
export default {
  async asyncData({ $http }) {
    const employees = await $http.$get('http://192.168.86.250:3000/employees/?format=api')
    return { employees }
  }
}
</script>
