/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.TitaniumIdentifier;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumLookupTableListItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:30:50.688776Z[UTC]")
public class TitaniumLookupTableListItem {
  public static final String SERIALIZED_NAME_IDENTIFIER = "identifier";
  @SerializedName(SERIALIZED_NAME_IDENTIFIER)
  private TitaniumIdentifier identifier;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_VALUE_FIELD = "valueField";
  @SerializedName(SERIALIZED_NAME_VALUE_FIELD)
  private String valueField;

  public TitaniumLookupTableListItem() { 
  }

  public TitaniumLookupTableListItem identifier(TitaniumIdentifier identifier) {
    
    this.identifier = identifier;
    return this;
  }

   /**
   * Get identifier
   * @return identifier
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumIdentifier getIdentifier() {
    return identifier;
  }


  public void setIdentifier(TitaniumIdentifier identifier) {
    this.identifier = identifier;
  }


  public TitaniumLookupTableListItem type(String type) {
    
    this.type = type;
    return this;
  }

   /**
   * Get type
   * @return type
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getType() {
    return type;
  }


  public void setType(String type) {
    this.type = type;
  }


  public TitaniumLookupTableListItem valueField(String valueField) {
    
    this.valueField = valueField;
    return this;
  }

   /**
   * Get valueField
   * @return valueField
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getValueField() {
    return valueField;
  }


  public void setValueField(String valueField) {
    this.valueField = valueField;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumLookupTableListItem titaniumLookupTableListItem = (TitaniumLookupTableListItem) o;
    return Objects.equals(this.identifier, titaniumLookupTableListItem.identifier) &&
        Objects.equals(this.type, titaniumLookupTableListItem.type) &&
        Objects.equals(this.valueField, titaniumLookupTableListItem.valueField);
  }

  @Override
  public int hashCode() {
    return Objects.hash(identifier, type, valueField);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumLookupTableListItem {\n");
    sb.append("    identifier: ").append(toIndentedString(identifier)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    valueField: ").append(toIndentedString(valueField)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("identifier");
    openapiFields.add("type");
    openapiFields.add("valueField");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumLookupTableListItem
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumLookupTableListItem.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumLookupTableListItem is not found in the empty JSON string", TitaniumLookupTableListItem.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumLookupTableListItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumLookupTableListItem` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `identifier`
      if (jsonObj.getAsJsonObject("identifier") != null) {
        TitaniumIdentifier.validateJsonObject(jsonObj.getAsJsonObject("identifier"));
      }
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      if (jsonObj.get("valueField") != null && !jsonObj.get("valueField").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `valueField` to be a primitive type in the JSON string but got `%s`", jsonObj.get("valueField").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumLookupTableListItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumLookupTableListItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumLookupTableListItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumLookupTableListItem.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumLookupTableListItem>() {
           @Override
           public void write(JsonWriter out, TitaniumLookupTableListItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumLookupTableListItem read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumLookupTableListItem given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumLookupTableListItem
  * @throws IOException if the JSON string is invalid with respect to TitaniumLookupTableListItem
  */
  public static TitaniumLookupTableListItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumLookupTableListItem.class);
  }

 /**
  * Convert an instance of TitaniumLookupTableListItem to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

