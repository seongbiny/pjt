# todo-vuex-app

### init project

```python
# Create Project
$ vue create todo-vuex-app
$ cd todo-vuex-app

# Add Vuex plugin in Vue CLI
$ vue add vuex
```

### 컴포넌트 작성

#### TodoListItem.vue

* 개별 todo 컴포넌트
* TodoList 컴포넌트의 자식 컴포넌트

```vue
// components/TodoListItem.vue

<template>
  <div>Todo</div>
</template>

<script>
export default {
    name: 'TodoListItem',
}
</script>
```

#### TodoList.vue

* todo 목록 컴포넌트
* TodoListItem 컴포넌트의 부모 컴포넌트

```vue
// components/TodoList.vue

<template>
  <div>
    <todo-list-item></todo-list-item>    
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
    name: 'TodoList',
    components: {
        TodoListItem,
    }
}
</script>
```

#### TodoForm.vue

* todo 데이터를 입력 받는 컴포넌트

```vue
// components/TodoForm.vue

<template>
  <div>Todo Form</div>
</template>

<script>
export default {
    name: 'TodoForm',
}
</script>
```

#### App.vue

* 최상위 컴포넌트
* TodoList, TodoForm 컴포넌트의 부모 컴포넌트

```vue
// App.vue

<template>
  <div>
    <h1>Todo List</h1>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
    
export default {
  name: 'App',
  compnents: {
      TodoList,
      TodoForm,
  }
}
</script>
```

### Create Todo

#### State 작성

```js
// index.js
export default new Vuex.Store({
  state: {
    todos: []
  }
}
```

#### TodoList 데이터 가져오기 & Computed로 변경

```vue
// TodoList.vue
<template>
  <div>
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
    ></todo-list-item> 
  </div>
</template>

<script>
// 1. vuex 모듈에서 mapState 메서드만 가져옴
import { mapState } from 'vuex'

export default {
  ...
  computed: {
    ...mapState([
      'todos' // state에 지정한 이름을 그대로 사용
    ])
  }
}
</script>
```

#### Pass Props (TodoList -> Todo)

```vue
// TodoList.vue

<template>
  <div>
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo" // v-for에서 받은게 오른쪽 todo, v-bind로 묶어서 보내는게 왼쪽 todo
    ></todo-list-item> 
  </div>
</template>
```

```vue
// TodoListItem.vue

<template>
  <div>
    {{ todo.title }} // 내려받은 prop 데이터
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  // props 데이터 등록
  props: {
    todo: {
      Object,
    }
  }
}
</script>
```

#### Actions & Mutations

```vue
// TodoForm.vue

<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle" // 입력 값이 자동으로 data에 연결된다
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null, //input태그와 연결
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      // todoItem.title이 있으면 = 뭐라도 적혀있으면
      if (todoItem.title) {
        // 입력받은 todoItem 값을 가지고 createTodo Action 함수 호출
        this.$store.dispatch('createTodo', todoItem) 
      }
      // 입력 받은게 아무것도 없으면 data는 그대로 null
      this.todoTitle = null
    }
  }
}
</script>
```

* createTodo 함수로 CREATE_TODO mutaion 함수 호출한다
* CREATE_TODO 함수는 state의 todo 데이터를 조작한다

```js
// index.js
export default new Vuex.Store({
  state: {
    todos: []
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem) // state 변경
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    }
  },
```

### Delete Todo

#### TodoListItem 컴포넌트

* deleteTodo action 함수 호출

```VUE
// TodoListItem.vue

<template>
  <div>
    <span>{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ...mapActions([
      'deleteTodo',
    ])
  }
}
</script>
```

#### Actions & Mutations

```js
// index.js
  mutations: {
	...
    DELETE_TODO: function(state, todoItem) {
      // todoItem이 첫 번째로 만나는 요소의 index를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 해당 index 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      state.todos.splice(index, 1)
    },
  actions: {
	...
    deleteTodo: function({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
```

### Update Todo

#### TodoListItem 컴포넌트

* updateTodoStatus action 함수 호출

```vue
// TodoListItem.vue

<template>
  <div>
    <!-- payload로 넘겨줬던 this.todo를 pass prop으로 변경해서 전달한다. -->
    <span @click="updateTodoStatus(todo)">{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
    
export default {
  ...
  methods: {
    ...mapActions([
      'deleteTodo',
      'updateTodoStatus',
    ])
  }
}
</script>
```

#### Actions & Mutations

```js
// index.js

mutations: {
    ...
    UPDATE_TODO_STATUS: function (state, todoItem) {
      // 3. 배열의 각 요소에 함수가 적용된 새로운 배열을 state의 todos에 할당
      state.todos = state.todos.map(todo => {
        // 1. 넘어온 todoItem과 현재 있는 stats의 todos의 요소가 일치하면
        if (todo === todoItem) {
          // completed의 상태를 변경한 새로운 object return
          return {
            ...todo,
            isCompleted: !todo.isCompleted
          }
        } else {
          // 2. 일치하지 않으면 기존 배열 return
          return todo
        }
      })
    }
  },
actions: {
  ...,
  updateTodoStatus: function ({ commit }, todoItem) {
    commit('UPDATE_TODO_STATUS', todoItem)
  }
},
```

#### 취소선 긋기

```vue
<template>
  <div>
    <span 
      @click="updateTodoStatus(todo)"
      :class="{ 'is-completed': todo.isCompleted }" //v-bind를 사용한 class binding
    >
    {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>
...
<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
```

### Getters

#### todo 개수 계산

```js
// index.js

  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    }
  },
```

```vue
// App.vue

<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>모든 투두 개수 : {{ allTodosCount }}</h2>
    <h2>완료된 투두 개수 : {{ completedTodosCount }}</h2>
    <h2>완료되지 않은 투두 개수 : {{ uncompletedTodosCount }}</h2>
    ...
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
    ...
computed: {
    // mapGetters 안에 정의한 메서드 중에서 아래 3개만 가져와서 Array에 추가한다.
    ...mapGetters([
      'completedTodosCount',
      'uncompletedTodosCount',
      'allTodosCount',
    ])
  }
</script>
```

### LocalStorage

#### vuex-persistedstate

* Vuex state를 자동으로 브라우저의 LocalStorage에 저장해주는 라이브러리 중 하나
* 페이지가 새로고침 되어도 Vuex state를 유지시킴

```python
$ npm install vuex-persistedstate
```

* 라이브러리 사용

```js
// index.js

import createPersistedState from "vuex-persistedstate"
```



